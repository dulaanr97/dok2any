<h1 align="center" id="title">DOK2ANY</h1>

<p id="description">dok2any is a Python package designed to convert DOK files, a chemical file format, to various other chemical structure formats using Open Babel.</p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Install the package using pip:</p>

<pre><code>pip install dok2any
</code></pre>

<h2>🔗 Dependencies:</h2>

<ul>
    <li>Python (>= 3.10)</li>
    <li>Open Babel (wheel package required)</li>
</ul>

<h2>📜 Usage:</h2>

<p>The dok2any package provides a command-line script to perform DOK file conversions.</p>

<pre><code>usage: dok2any [-h] -idok IDOK -oformat OFORMAT -odir ODIR

Convert DOK files to specified output format using Open Babel.

optional arguments:
  -h, --help                 show this help message and exit
  -idok IDOK, --idok IDOK    Path to the folder containing DOK files (required)
  -oformat OFORMAT, --oformat OFORMAT  Output format for conversion (e.g., mol2, pdb, sdf) (required)
  -odir ODIR, --odir ODIR    Path to the output directory (required)
</code></pre>

<h3>Example Usage:</h3>

<pre><code>dok2any -idok /path/to/dok/files -oformat mol2 -odir /path/to/output
</code></pre>

<p>This command will convert all DOK files in the <code>/path/to/dok/files</code> folder to MOL2 format and save the output files in the <code>/path/to/output</code> directory.</p>

<h2>📄 License:</h2>

<p>dok2any is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more information.</p>


