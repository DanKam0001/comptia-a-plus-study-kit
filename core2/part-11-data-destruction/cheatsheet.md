# Core 2, Part 11: Data Destruction and Disposal

**Objective 2.9** (220-1202): *Compare and contrast common data destruction and disposal methods.*
Domain: Security (28% of the exam).

## The core idea

Deleting a file removes its entry in the index, not the data. Until it is overwritten, recovery software can bring it back. Before a drive leaves your control you either **erase it so it can be reused**, or **destroy it**.

## Physical destruction of hard drives

| Method | What it does | Notes |
|---|---|---|
| Drilling | Holes through the platters | Cheap and quick, but less thorough than shredding |
| Shredding | Industrial shredder cuts the drive into small pieces | Very thorough. Works on HDDs, SSDs, phones |
| Degaussing | Very strong magnet scrambles magnetic data | **Magnetic media only** (hard drives, tape). Does **nothing** to an SSD, which stores data in flash chips |
| Incineration | Burning at high temperature | Should be done by a licensed facility |

## Recycling or repurposing best practices

| Method | What it does | Safe for sensitive data? |
|---|---|---|
| Standard format (quick format) | Builds a new empty index only. (A full format in Windows Vista and later also writes zeros, but the exam treats standard format as not safe) | **No.** Data remains recoverable |
| Low-level format | Writes over every sector (usually with zeros) | Yes, for reuse. Slower |
| Erasing / wiping | Software overwrites the whole drive with zeros or random data, sometimes several passes | Yes, for reuse |

- Wipe when the drive will be **reused, sold or donated**.
- Destroy when the drive will **never be used again**, has failed (can't be wiped), or holds **very sensitive** data.
- **SSD note:** flash drives move data around internally, so plain overwriting can miss some. Use the maker's secure erase tool (or encryption plus key destruction), or physically destroy it.
- Many organisations **wipe first, then destroy**.

## Outsourcing concepts

- **Third-party vendor:** an outside company collects drives and destroys or recycles them.
- **Certification of destruction / recycling:** signed proof listing the drives (usually by serial number), the date and the method. Keep it as evidence.
- Keep a **chain of custody** record of who held the drives until destruction (see Core 2 Part 15 for chain of custody in incident response).

## Regulatory and environmental requirements

- Laws and company policy set how long data must be kept and how it must be destroyed. Regulated data includes personal, health and payment card data (see Core 2 Part 15).
- Electronics contain batteries and chemicals. Use approved e-waste recyclers, never the normal bin.
- Follow your organisation's policy, which can be stricter than the law.

## Common scenarios

| Scenario | Likely answer |
|---|---|
| Selling old laptops that held customer data | Wipe (full overwrite), not delete or quick format |
| Failed drive that can't be wiped | Physically destroy it |
| Old SSD, someone suggests a degausser | Won't work. Secure erase or shred |
| Outside company destroys the drives | Get a certificate of destruction |
| Is a quick format enough to give a PC away? | No |
| Which method works only on magnetic media? | Degaussing |
