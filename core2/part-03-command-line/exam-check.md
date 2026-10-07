# Exam check: The Windows Command Line

Cover the answers and try each one out loud first.

**1.** A user can't get online, and you need to see the computer's IP address from the command line. Which command do you run?
<details><summary>Answer</summary>`ipconfig`. Add `/all` to see the DNS servers too.</details>

**2.** Windows keeps showing strange errors, and you think important system files are damaged. Which command scans and repairs them?
<details><summary>Answer</summary>`sfc /scannow`, run in an administrator Command Prompt. `chkdsk` checks the drive, not the Windows files.</details>

**3.** You need to copy a large folder to a backup drive and keep all of its subfolders. Which command is built for this?
<details><summary>Answer</summary>`robocopy` with the `/E` switch.</details>

## More practice (written for this kit)

**4.** Which command shows every router between a computer and a website?
<details><summary>Answer</summary>`tracert`. `pathping` does the same and also shows packet loss at each hop.</details>

**5.** A technician needs to map a shared folder to drive Z: from the command line. Which command?
<details><summary>Answer</summary>`net use Z: \\server\share`.</details>

**6.** A drive shows read errors. Which command checks it and recovers readable data from bad sectors?
<details><summary>Answer</summary>`chkdsk /r`.</details>

**7.** A new Group Policy setting hasn't reached a PC yet. How do you force it, and then check what applied?
<details><summary>Answer</summary>`gpupdate /force`, then `gpresult /r`.</details>

**8.** Which command lists the active connections and listening ports, with process IDs?
<details><summary>Answer</summary>`netstat -ano`.</details>

**9.** After moving a laptop to a new network, it still has its old IP address. Which two commands fix it?
<details><summary>Answer</summary>`ipconfig /release` then `ipconfig /renew`.</details>

**10.** Which command shows the Windows version and build number in a small window?
<details><summary>Answer</summary>`winver`.</details>
