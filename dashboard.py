import os
from junitparser import JUnitXml

REPORT_DIR = "reports"
OUTPUT_DIR = "dashboard"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "summary.html")

os.makedirs(OUTPUT_DIR, exist_ok=True)

total_tests = total_failures = total_errors = total_skipped = 0
rows = ""

for file in os.listdir(REPORT_DIR):
    if file.endswith(".xml"):
        xml = JUnitXml.fromfile(os.path.join(REPORT_DIR, file))
        total_tests += xml.tests
        total_failures += xml.failures
        total_errors += xml.errors
        total_skipped += xml.skipped
        status = "PASS" if xml.failures == 0 and xml.errors == 0 else "FAIL"
        rows += f"""
        <tr>
            <td>{file}</td>
            <td>{xml.tests}</td>
            <td>{xml.failures}</td>
            <td>{xml.errors}</td>
            <td>{xml.skipped}</td>
            <td>{status}</td>
        </tr>
        """

html = f"""
<html>
<head>
<title>Test Summary Dashboard</title>
<style>
body {{ font-family: Arial; }}
table {{ border-collapse: collapse; width: 80%; }}
th, td {{ border: 1px solid black; padding: 8px; text-align: center; }}
th {{ background-color: #f2f2f2; }}
</style>
</head>
<body>
<h1>Jenkins Test Summary</h1>
<ul>
<li>Total Tests: {total_tests}</li>
<li>Total Failures: {total_failures}</li>
<li>Total Errors: {total_errors}</li>
<li>Total Skipped: {total_skipped}</li>
</ul>
<table>
<tr>
<th>Category</th>
<th>Tests</th>
<th>Failures</th>
<th>Errors</th>
<th>Skipped</th>
<th>Status</th>
</tr>
{rows}
</table>
</body>
</html>
"""

with open(OUTPUT_FILE, "w") as f:
    f.write(html)
print("Dashboard generated at:", OUTPUT_FILE)
