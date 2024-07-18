<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dok2any</title>
</head>
<body>
    <h1>dok2any</h1>
    <p><strong>dok2any</strong> is a Python package designed to convert DOK files, a chemical file format, to various other chemical structure formats using Open Babel.</p>

    <h2>Features</h2>
    <ul>
        <li>Converts DOK files to popular formats like MOL2, PDB, and SDF.</li>
        <li>Extracts atomic coordinates and types from DOK files.</li>
        <li>Uses Open Babel for format conversions.</li>
        <li>Supports batch processing of DOK files in a directory.</li>
    </ul>

    <h2>Installation</h2>
    <p><strong>dok2any</strong> can be installed using pip:</p>
    <pre><code>pip install dok2any</code></pre>

    <h3>Dependencies:</h3>
    <ul>
        <li>Python (>= 3.10)</li>
        <li>Open Babel (wheel package required)</li>
    </ul>

    <h2>Usage</h2>
    <p>The dok2any package provides a command-line script to perform DOK file conversions.</p>
    <pre><code>usage: dok2any [-h] -idok IDOK -oformat OFORMAT -odir ODIR

Convert DOK files to specified output format using Open Babel.

optional arguments:
  -h, --help                 show this help message and exit
  -idok IDOK, --idok IDOK    Path to the folder containing DOK files (required)
  -oformat OFORMAT, --oformat OFORMAT  Output format for conversion (e.g., mol2, pdb, sdf) (required)
  -odir ODIR, --odir ODIR    Path to the output directory (required)</code></pre>

    <h3>Example usage:</h3>
    <pre><code>dok2any -idok /path/to/dok/files -oformat mol2 -odir /path/to/output</code></pre>

    <p>This command will convert all DOK files in the <code>/path/to/dok/files</code> folder to MOL2 format and save the output files in the <code>/path/to/output</code> directory.</p>

    <h2>License</h2>
    <p>dok2any is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more information.</p>
</body>
</html>
