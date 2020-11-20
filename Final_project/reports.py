#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(file, title, info):
    style = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, style["h1"])
    report_info = Paragraph(info, style["BodyText"])
    blank_line = Spacer(1, 20)
    report.build([report_title, blank_line, report_info, blank_line])