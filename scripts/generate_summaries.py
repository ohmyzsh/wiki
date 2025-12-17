#!/usr/bin/env python3
"""Generate reports/summary.md and reports/summary.csv from `reports/` files.

Usage: python3 scripts/generate_summaries.py [--reports-dir reports]
"""
import os
import re
import csv
import argparse
import tempfile


def parse_report(path):
    txt = ''
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            txt = f.read()
    except Exception:
        return None

    def find(rx):
        m = re.search(rx, txt)
        return m.group(1).strip() if m else ''

    return {
        'Shows username': find(r'Shows username:\s*([^\n]+)'),
        'Shows hostname': find(r'Shows hostname:\s*([^\n]+)'),
        'Shows time/date': find(r'Shows time/date:\s*([^\n]+)'),
        'Shows last command failure': find(r'Shows last command failure:\s*([^\n]+)'),
        'PWD style': find(r'PWD style:\s*([^\n]+)'),
        'Other info': find(r'Other info:\s*([^\n]+)'),
    }


def write_atomic(path, data, mode='w', encoding='utf-8'):
    dname = os.path.dirname(path) or '.'
    fd, tmp = tempfile.mkstemp(dir=dname)
    with os.fdopen(fd, mode, encoding=encoding) as f:
        f.write(data)
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)

def generate_md(reports_dir,out_md,out_csv):
    """This will generate the Markdown file

    Args:
        reports_dir (str): directory of all reports
        out_md (str): Where the markdown file will be created
        out_csv (str): Where the CSV file will be created
    """
    files = sorted([f for f in os.listdir(reports_dir) if os.path.isfile(os.path.join(reports_dir, f))])
    rows = []
    for fn in files:
        # skip file if it has the name of the summary files
        # or has extension .md or .csv(most likely are summary files)
        if fn in (os.path.basename(out_md), os.path.basename(out_csv)) or fn.endswith(".csv") or fn.endswith(".md"): continue
        path = os.path.join(reports_dir, fn)
        parsed = parse_report(path)
        if parsed is None:
            continue
        rows.append((fn, parsed))
    # Markdown
    md_lines = ['# Reports summary', '']
    md_lines.append('| Report | Username | Hostname | Time/Date | Last Failure | PWD style | Other info |')
    md_lines.append('|---|---:|---:|---:|---:|---|---|')
    for fn, vals in rows:
        md_lines.append('| {} | {} | {} | {} | {} | {} | {} |'.format(
            fn,
            vals.get('Shows username') or '-',
            vals.get('Shows hostname') or '-',
            vals.get('Shows time/date') or '-',
            vals.get('Shows last command failure') or '-',
            vals.get('PWD style') or '-',
            vals.get('Other info') or '-'
        ))
    md_text = '\n'.join(md_lines) + '\n'
    write_atomic(out_md, md_text)

def generate_csv(reports_dir, out_md, out_csv):
    files = sorted([f for f in os.listdir(reports_dir) if os.path.isfile(os.path.join(reports_dir, f))])
    rows = []
    for fn in files:
        # skip summary files if present
        if fn in (os.path.basename(out_md), os.path.basename(out_csv)) or fn.endswith(".csv") or fn.endswith(".md"): continue
        path = os.path.join(reports_dir, fn)
        parsed = parse_report(path)
        if parsed is None:
            continue
        rows.append((fn, parsed))
    # CSV
    csv_path = out_csv
    with tempfile.NamedTemporaryFile('w', delete=False, dir=os.path.dirname(csv_path), encoding='utf-8', newline='') as tmpf:
        w = csv.writer(tmpf)
        w.writerow(['Report','Shows username','Shows hostname','Shows time/date','Shows last command failure','PWD style','Other info'])
        for fn, vals in rows:
            w.writerow([
                fn,
                vals.get('Shows username') or '-',
                vals.get('Shows hostname') or '-',
                vals.get('Shows time/date') or '-',
                vals.get('Shows last command failure') or '-',
                vals.get('PWD style') or '-',
                vals.get('Other info') or '-',
            ])
    os.replace(tmpf.name, csv_path)


def main():
    p = argparse.ArgumentParser(description='Generate reports/summary.md and reports/summary.csv')
    p.add_argument('--reports-dir', default='reports', help='Directory containing report files')
    p.add_argument('-m','--make-md',help="Enables creating a MD file",action='store_true')
    p.add_argument('-c','--make-csv',help="Enables creating a csv file",action='store_true')
    p.add_argument('--out-md', default=os.path.join('reports','summary.md'), help='Output markdown file')
    p.add_argument('--out-csv', default=os.path.join('reports','summary.csv'), help='Output csv file')
    args = p.parse_args()

    reports_dir = args.reports_dir
    if not os.path.isdir(reports_dir):
        raise SystemExit(f'reports dir not found: {reports_dir}')
    #generating files:
    if args.make_csv:
        generate_csv(reports_dir, args.out_md, args.out_csv)
        print('WROTE', args.out_csv)
    if args.make_md:
        generate_md(reports_dir, args.out_md, args.out_csv)
        print('WROTE', args.out_md)


if __name__ == '__main__':
    main()
