# markdownHelp[er]
Convert argpase &amp; equivalent help documents to markdown.

Usage: `python3 markdownHelper.py <script_name>`  
Outputs to same directory as markdownHelper.py

More features to come, such as

 - Insertion into existing markdown files using hidden tags
 - Output specification
 - Additional backtick/code formatting

**Current known issues:**

 - Single dash flags aren't formatted with backticks if they either are prefixed with an open bracket or suffixed with a comma.
 - Brackets duplicating?


## Example Output:

 - Running this `./markdownHelper.py ../updateAll/updateAll.py` [#](https://github.com/Ports-Exposed/updateAll)

 - Changes this:
```bash
$  ../updateAll/updateAll.py -h
usage: updateAll [-h] [-H] [-v] [--debug [DEBUG]] {update,up,count,ct,check-broken,ck} ...

Universal Package Manager Update Utility

positional arguments:
  {update,up,count,ct,check-broken,ck}
                        Operation to perform
    update (up)         Update packages
    count (ct)          Count upgradable packages
    check-broken (ck)   Check for broken packages where supported

options:
  -h, --help            show this help message and exit
  -H, --full-help       Display full updateAll help
  -v, --version         show program's version number and exit
  --debug [DEBUG]       Debug
  
$  ../updateAll/updateAll.py update -h
usage: updateAll update [-h] [-c] [-p] [-S] [-s SKIP [SKIP ...]] [-V] [package_managers ...]

positional arguments:
  package_managers      Whitelist of package managers to use

options:
  -h, --help            show this help message and exit
  -c, --check-broken    Check for broken packages after updating where supported
  -p, --simple          Don't use Live Table output for Package Manager Status
  -S, --simulate        Dry run/simulate update process
  -s SKIP [SKIP ...], --skip SKIP [SKIP ...]
                        Skip specified package managers
  -V, --verbose         Enable verbose output
  
$  ../updateAll/updateAll.py count -h
usage: updateAll count [-h] [-p] [-s SKIP [SKIP ...]] [-V] [package_managers ...]

positional arguments:
  package_managers      Whitelist of package managers to use

options:
  -h, --help            show this help message and exit
  -p, --simple          Don't use Live Table output for Package Manager Status
  -s SKIP [SKIP ...], --skip SKIP [SKIP ...]
                        Skip specified package managers
  -V, --verbose         Enable verbose output

$ ../updateAll/updateAll.py check-broken -h
usage: updateAll check-broken [-h] [-p] [-S] [-s SKIP [SKIP ...]] [-V] [package_managers ...]

positional arguments:
  package_managers      Whitelist of package managers to use

options:
  -h, --help            show this help message and exit
  -p, --simple          Don't use Live Table output for Package Manager Status
  -S, --simulate        Dry run/simulate check process
  -s SKIP [SKIP ...], --skip SKIP [SKIP ...]
                        Skip specified package managers
  -V, --verbose         Enable verbose output
```

 - Into this:

<!--HELP GEN START-->
## Help Documentation
| Operation | Usage | Positional Arguments | Options |
| --- | --- | --- | --- |
| **Main** | updateAll [-h] [-H] [-v] [--debug [DEBUG]] {update,up,count,ct,check-broken,ck} ... Universal Package Manager Update Utility | {update,up,count,ct,check-broken,ck}<br> Operation to perform<br> update (up)         Update packages<br> count (ct)          Count upgradable packages<br> check-broken (ck)   Check for broken packages where supported<br> <br>  | -h, `--help`            show this help message and exit<br> -H, `--full-help`       Display full updateAll help<br> -v, `--version`         show program's version number and exit<br> --debug [DEBUG]       Debug<br>  |
| **update** | updateAll update [-h] [-c] [-p] [-S] [-s SKIP [SKIP ...]] [-V] [package_managers ...] | package_managers      Whitelist of package managers to use<br> <br>  | -h, `--help`            show this help message and exit<br> -c, `--check-broken`    Check for broken packages after updating where<br> supported<br> -p, `--simple`          Don't use Live Table output for Package Manager Status<br> -S, `--simulate`        Dry run/simulate update process<br> -s SKIP [SKIP ...], `--skip` SKIP [SKIP ...]<br> Skip specified package managers<br> -V, `--verbose`         Enable verbose output<br>  |
| **count** | updateAll count [-h] [-p] [-s SKIP [SKIP ...]] [-V] [package_managers ...] | package_managers      Whitelist of package managers to use<br> <br>  | -h, `--help`            show this help message and exit<br> -p, `--simple`          Don't use Live Table output for Package Manager Status<br> -s SKIP [SKIP ...], `--skip` SKIP [SKIP ...]<br> Skip specified package managers<br> -V, `--verbose`         Enable verbose output<br>  |
| **check-broken** | updateAll check-broken [-h] [-p] [-S] [-s SKIP [SKIP ...]] [-V] [package_managers ...] | package_managers      Whitelist of package managers to use<br> <br>  | -h, `--help`            show this help message and exit<br> -p, `--simple`          Don't use Live Table output for Package Manager Status<br> -S, `--simulate`        Dry run/simulate check process<br> -s SKIP [SKIP ...], `--skip` SKIP [SKIP ...]<br> Skip specified package managers<br> -V, `--verbose`         Enable verbose output<br>  |
<!--HELP GEN END-->