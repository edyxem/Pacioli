from django.shortcuts import render
from django.http import HttpResponse
from recettes.models import Recette
from depenses.models import Depense
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from datetime import date


def journal(request):
    date_debut = request.GET.get('date_debut', '')
    date_fin = request.GET.get('date_fin', '')
    recettes = Recette.objects.all()
    depenses = Depense.objects.all()
    if date_debut:
        recettes = recettes.filter(date__gte=date_debut)
        depenses = depenses.filter(date__gte=date_debut)
    if date_fin:
        recettes = recettes.filter(date__lte=date_fin)
        depenses = depenses.filter(date__lte=date_fin)
    return render(request, 'rapport.html', {
        'action': 'journal',
        'recettes': recettes,
        'depenses': depenses,
        'date_debut': date_debut,
        'date_fin': date_fin,
    })


def bilan(request):
    total_recettes = sum(r.montant for r in Recette.objects.all())
    total_depenses = sum(d.montant for d in Depense.objects.all())
    solde = total_recettes - total_depenses
    return render(request, 'rapport.html', {
        'action': 'bilan',
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'solde': solde,
    })


def etat_recettes(request):
    recettes = Recette.objects.all()
    total = sum(r.montant for r in recettes)
    return render(request, 'rapport.html', {
        'action': 'etat_recettes',
        'recettes': recettes,
        'total': total,
    })


def etat_depenses(request):
    depenses = Depense.objects.all()
    total = sum(d.montant for d in depenses)
    return render(request, 'rapport.html', {
        'action': 'etat_depenses',
        'depenses': depenses,
        'total': total,
    })


def rapport_global(request):
    recettes = Recette.objects.all()
    depenses = Depense.objects.all()
    total_recettes = sum(r.montant for r in recettes)
    total_depenses = sum(d.montant for d in depenses)
    solde = total_recettes - total_depenses
    return render(request, 'rapport.html', {
        'action': 'rapport_global',
        'recettes': recettes,
        'depenses': depenses,
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'solde': solde,
    })


def bilan_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bilan_pacioli.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)

    styles = getSampleStyleSheet()
    elements = []

    # ── Titre
    titre_style = ParagraphStyle('titre', parent=styles['Title'],
                                  fontSize=22, textColor=colors.HexColor('#0a0a0a'),
                                  spaceAfter=6, alignment=TA_CENTER)
    sous_titre_style = ParagraphStyle('sous_titre', parent=styles['Normal'],
                                       fontSize=11, textColor=colors.HexColor('#888888'),
                                       spaceAfter=20, alignment=TA_CENTER)

    elements.append(Paragraph("PACIOLI", titre_style))
    elements.append(Paragraph(f"Bilan simplifié — {date.today().strftime('%d/%m/%Y')}", sous_titre_style))
    elements.append(Spacer(1, 0.5*cm))

    # ── Données
    recettes = Recette.objects.all()
    depenses = Depense.objects.all()
    total_recettes = sum(r.montant for r in recettes)
    total_depenses = sum(d.montant for d in depenses)
    solde = total_recettes - total_depenses

    # ── KPI tableau
    kpi_data = [
        ['TOTAL RECETTES', 'TOTAL DÉPENSES', 'RÉSULTAT NET'],
        [
            f"{total_recettes:,.0f} XOF",
            f"{total_depenses:,.0f} XOF",
            f"{'+' if solde >= 0 else ''}{solde:,.0f} XOF"
        ],
    ]
    kpi_table = Table(kpi_data, colWidths=[5.5*cm, 5.5*cm, 5.5*cm])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0a0a0a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWHEIGHT', (0, 0), (-1, -1), 0.8*cm),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, 1), 12),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#1ea97c')),
        ('TEXTCOLOR', (1, 1), (1, 1), colors.HexColor('#d9534f')),
        ('TEXTCOLOR', (2, 1), (2, 1),
         colors.HexColor('#1ea97c') if solde >= 0 else colors.HexColor('#d9534f')),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#e8e8e8')),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.HexColor('#333333')),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    elements.append(kpi_table)
    elements.append(Spacer(1, 0.8*cm))

    # ── Tableau recettes
    section_style = ParagraphStyle('section', parent=styles['Heading2'],
                                    fontSize=13, textColor=colors.HexColor('#0a0a0a'),
                                    spaceBefore=16, spaceAfter=8)
    elements.append(Paragraph("Recettes", section_style))

    rec_data = [['Date', 'Description', 'Client', 'Montant']]
    for r in recettes:
        rec_data.append([
            str(r.date),
            r.description,
            str(r.client) if r.client else '—',
            f"+{r.montant:,.0f} XOF",
        ])
    if len(rec_data) == 1:
        rec_data.append(['—', 'Aucune recette', '—', '—'])

    rec_table = Table(rec_data, colWidths=[2.5*cm, 7*cm, 4*cm, 3*cm])
    rec_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f0f0f0')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (3, 0), (3, -1), 'RIGHT'),
        ('TEXTCOLOR', (3, 1), (3, -1), colors.HexColor('#1ea97c')),
        ('FONTNAME', (3, 1), (3, -1), 'Helvetica-Bold'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafafa')]),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#e8e8e8')),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(rec_table)
    elements.append(Spacer(1, 0.5*cm))

    # ── Tableau dépenses
    elements.append(Paragraph("Dépenses", section_style))

    dep_data = [['Date', 'Description', 'Fournisseur', 'Montant']]
    for d in depenses:
        dep_data.append([
            str(d.date),
            d.description,
            str(d.fournisseur) if d.fournisseur else '—',
            f"-{d.montant:,.0f} XOF",
        ])
    if len(dep_data) == 1:
        dep_data.append(['—', 'Aucune dépense', '—', '—'])

    dep_table = Table(dep_data, colWidths=[2.5*cm, 7*cm, 4*cm, 3*cm])
    dep_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f0f0f0')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (3, 0), (3, -1), 'RIGHT'),
        ('TEXTCOLOR', (3, 1), (3, -1), colors.HexColor('#d9534f')),
        ('FONTNAME', (3, 1), (3, -1), 'Helvetica-Bold'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fafafa')]),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#e8e8e8')),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(dep_table)
    elements.append(Spacer(1, 0.8*cm))

    # ── Résultat final
    resultat_couleur = colors.HexColor('#1ea97c') if solde >= 0 else colors.HexColor('#d9534f')
    resultat_data = [[
        f"{'✓ Bénéfice' if solde >= 0 else '⚠ Déficit'}",
        f"{'+' if solde >= 0 else ''}{solde:,.0f} XOF"
    ]]
    resultat_table = Table(resultat_data, colWidths=[12*cm, 4.5*cm])
    resultat_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8f8f8')),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TEXTCOLOR', (0, 0), (-1, -1), resultat_couleur),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('BOX', (0, 0), (-1, -1), 1, resultat_couleur),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 16),
    ]))
    elements.append(resultat_table)

    doc.build(elements)
    return response