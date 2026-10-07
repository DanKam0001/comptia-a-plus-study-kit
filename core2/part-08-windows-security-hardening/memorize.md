# Memorise list: Windows Security Settings and Workstation Hardening (Core 2, Part 8)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core2_part08.csv`](../../flashcards/core2_part08.csv) (import into Anki or any flashcard app).

## Accounts and sign-in

| Question | Answer |
|---|---|
| Account types (5) | Local, Microsoft, standard, administrator, guest (plus legacy power user) |
| Which account is off by default? | Guest |
| Standard user can / cannot | Run programs / change system settings |
| UAC does | Asks permission before big changes |
| Six log-in options | Username and password, PIN, fingerprint, facial recognition, SSO, passwordless (Windows Hello) |
| A Windows Hello PIN works | Only on that device |

## Defender and firewall

| Question | Answer |
|---|---|
| Defender definitions are | The list of known threats, updated through Windows Update |
| Firewall port security vs application security | Allow or block ports vs allow or block programs |
| Open the advanced firewall console | `wf.msc` |

## Permissions

| Question | Answer |
|---|---|
| NTFS vs share permissions | NTFS = on the disk, always applies. Share = over the network only |
| Both apply: which wins? | The most restrictive |
| Inheritance | Files and folders take permissions from their parent |
| Move to a different volume | Takes the destination folder's permissions |
| Move within the same volume | Keeps original permissions |

## Encryption

| Question | Answer |
|---|---|
| BitLocker | Whole drive. Usually uses the TPM. Keep the recovery key |
| BitLocker To Go | USB and removable drives |
| EFS | Single files or folders, per user |
| Data at rest | Stored data |

## Active Directory tasks (7)

Join a domain; assign a log-in script; move objects within OUs; assign home folders; apply Group Policy; select security groups; configure folder redirection.

## Hardening checklist

| Group | Items |
|---|---|
| Password considerations (5) | Length, character types, uniqueness, complexity, expiration |
| End-user best practices (5) | Screensaver locks, log off, protect hardware, secure PII and passwords, password managers |
| Account management (6) | Restrict permissions, restrict log-in times, disable guest, failed-attempts lockout, timeout/screen lock, account expiration dates |
| Other (3) | Change default administrator account and password, disable AutoRun, disable unused services |
