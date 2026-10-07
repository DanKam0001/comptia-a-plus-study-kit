# Exam check: Windows Security Settings and Workstation Hardening

Cover the answers and try each one out loud first.

**1.** A company laptop is stolen, and the company wants the files on it to be unreadable to the thief. What should have been turned on?
<details><summary>Answer</summary>BitLocker. (Why: it encrypts the whole drive, so a thief who removes it still cannot read the files without the key.)</details>

**2.** A company wants all 200 PCs to lock their screens after ten minutes, without visiting each one. What is the best tool?
<details><summary>Answer</summary>Group Policy. (Why: Group Policy in Active Directory pushes settings to every computer in the domain at once.)</details>

**3.** A user has Full Control in the NTFS permissions on a shared folder, but only Read in the share permissions. What can they do over the network?
<details><summary>Answer</summary>Read files only. (Why: when share and NTFS permissions both apply over the network, the most restrictive one wins.)</details>

## More practice (written for this kit)

**4.** A user wants to encrypt a USB flash drive before carrying files on it. Which Windows tool?
<details><summary>Answer</summary>BitLocker To Go.</details>

**5.** A contractor starts a three month job. What account setting prevents the account being usable after the contract ends?
<details><summary>Answer</summary>An account expiration date.</details>

**6.** An account is being attacked by someone guessing passwords. Which setting slows this down?
<details><summary>Answer</summary>Failed-attempts lockout.</details>

**7.** Plugging in a USB drive makes a program start by itself. Which setting should be disabled?
<details><summary>Answer</summary>AutoRun.</details>

**8.** Which Windows feature lets a user sign in with a face or fingerprint instead of a password?
<details><summary>Answer</summary>Windows Hello (passwordless sign-in).</details>

**9.** A user needs to install a program but only has a standard account. What is the correct approach?
<details><summary>Answer</summary>Use run as administrator (enter an administrator's credentials at the UAC prompt), rather than giving the user an administrator account for daily use.</details>
