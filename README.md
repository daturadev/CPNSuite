
# SSNope
---
*SSNope is a cybersecurity/software-development POC written using Python and JSON as a storage solution. It is not intended to be used for illegitimate purposes and was created out of legitimate-interest.*

This Python script serves as a simple tool for generating and validating Social Security Numbers (SSNs) and Credit Privacy Numbers (CPNs) based on state-specific area mappings. It utilizes various libraries, including colorama for colored terminal output, random for generating random numbers, and selenium for web scraping to validate the generated numbers.

---

<b>Key Concepts:</b>
- Data Handling: <i>The script reads state-area mappings from a JSON file, allowing for dynamic SSN generation based on the specified state.</i>
- Random Number Generation: <i>It generates random SSNs by combining area numbers, group numbers, and serial numbers.</i>
- Web Scraping: <i>The script uses Selenium to check for validity of generated SSNs by scraping a verification website's results.</i>
- Command-Line Interface: <i>It accepts command-line arguments for state and count, enhancing usability.<i>

<b>Code Structure</b>

The code is structured into several key components:

- Imports: <i>Necessary libraries are imported at the beginning.</i>
- Data Loading: <i>The script attempts to load state-area mappings from a JSON file.</i>
- Functions: <i>Several functions are defined for specific tasks, including clearing the console, generating SSNs, and validating them.</i>
- Main Execution: <i>The script's main logic is encapsulated in the main() function, which orchestrates the flow of the program</i>

Be aware:
- **18 U.S. Code § 1014**: Making false statements on a credit application is a crime.
- **Identity Theft**: If the number generated so happens to be a legitimate number (children, deceased individuals, prisoners, ...) this does legally qualify as identity theft if-utilized... This method, however, solely generates unused combinations.
>("Scammers can also create fake SSNs that have not
>yet been issued by the government. This is done by
>using algorithms to generate 9-digit numbers. These
>numbers are then run against databases to find out
>which numbers could pose as SSNs.")
> -- [crediful.com](https://www.crediful.com/credit-privacy-number-cpn/)

<i>Again, this program is intended for educational used as a PoC. Please treat it as such, examining how the code applies the concepts of CPNs and SSN structures to exploit an surprisingly simple system.</i>

---


## Acknowledgements

 - [Structure of Social Security Numbers; Jerry Crowe, Barbara Bennett](https://web.archive.org/web/20100816142710/http://w2.eff.org/Privacy/ID_SSN_fingerprinting/ssn_structure.articles)
 - [Steve Morse's Online Tool](https://stevemorse.org/ssn/ssn.html)
 - [SSN Generator (The most-useful of MANY generators/validators found. Once I realized that the only real important segment is the first three digits, I began to prefer this. Allows for batch-generation.)](https://www.thinkcalculator.com/generator/social-security-number.php)

- [More information on SSN principles, pre-2011 randomization](https://www.ssn-verify.com/decode-ssn)

- [Randomization as a new security measure, 2011](https://www.ssn-verify.com/ssn-randomization)

<sub>much-needed. bit late, lol.</sub>

---


## FAQ

#### What is a CPN?

CPN (Credit Privacy Numbers) are those valid social security numbers with no formal assignments. With the way that the US credit system is structured, this leaves these stray, nine-digit codes open to be manipulated and used. 

#### Is it legal?

I'm not a lawyer. I get the impression that it's in a grey-area. The banks clearly hate it. When searching for information, I made sure not to provide URLs to credit bureaus, who wouldn't specifically claim them to be illegal but used elaborate wording to effectively fear-monger. They do provide some effective alternatives to repairing your actual credit.

---

TODO:
- Bypass Cloudfare and do away with the horrendous curse of Selenium automation

---

To be continued. Thanks.

-- daturadev
