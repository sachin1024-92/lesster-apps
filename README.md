# Lesster Apps

Small, privacy-first Android utilities for everyday problems in India. Most apps work offline and keep your data on your phone.

**Privacy policies (GitHub Pages):** https://sachin1024-92.github.io/lesster-apps/  
**Contact:** princendlesster@gmail.com

This repository hosts the public privacy policies and listing helpers for the Lesster suite. App source follows the same Kotlin stack as [FloatNote](https://github.com/sachin1024-92/daily-motivation-ai/tree/main/floating-notepad) (`play` + `foss` flavours, AdMob/Billing where noted, minSdk 26 / targetSdk 36).

## Apps

| App | Package | What it does | Network | Monetization |
|---|---|---|---|---|
| **SahiPix: Exam Form Photo & Doc Kit** | `app.sahipix.formkit` | Resize/compress photos, signatures and docs to the exact size and format exam portals require | Ads + Billing only | One-time Pro (~₹49–99) removes banner |
| **Scam Check** | `india.scamcheck` | Paste or share a suspicious message/link; on-device risk score in English, Hindi or Hinglish | Models + Billing | Family Pack one-time (~₹99) |
| **VaultMask: Private ID Vault** | `app.vaultmask.privateid` | Encrypted offline vault for ID copies; mask Aadhaar; purpose-stamp shared copies | Offline | One-time Pro (~₹149) |
| **Gig Hisaab: Gig Earnings Tracker** | `app.gighisaab.ledger` | Track delivery/ride earnings, fuel and expenses; real net pay per hour and per km | Ads + Billing | Pro yearly subscription |
| **Family Verify** | `app.familyverify` | Family safe word, panic script, and steps against voice-clone / fake-emergency / “digital arrest” scams | Offline | Free, no ads |
| **Safe QR & UPI Scanner** | `in.successtips.safeqr` | Scan a QR and see where it leads and who a UPI payee is before you pay | Ads + Billing | One-time Pro (~₹49) |
| **Attendance & Bunk Planner** | `app.bunkplanner.attendance` | Per-subject attendance and how many classes you can skip while staying above 75% | Offline | One-time Pro (~₹49) |

## Design rules (shared with FloatNote)

- Core task works without an account and without uploading user content
- No `READ_MEDIA_IMAGES` / broad storage — Photo Picker and SAF only where needed
- `play` flavour may show a single banner on browse screens; never on the edit/export or scan critical path
- `foss` flavour strips Google SDKs and Internet permission where the product allows it
- Secrets and keystores stay in CI env vars; secret-scan must pass
- Release APK target: under 8 MB for single-purpose tools

## Privacy pages

Policies are generated from `gen.py` (last updated 17 November 2026):

```bash
python3 gen.py
# writes out/index.html and out/apps/<slug>/privacy/
```

Published paths:

- https://sachin1024-92.github.io/lesster-apps/apps/sahipix/privacy/
- https://sachin1024-92.github.io/lesster-apps/apps/scam-check/privacy/
- https://sachin1024-92.github.io/lesster-apps/apps/vaultmask/privacy/
- https://sachin1024-92.github.io/lesster-apps/apps/gig-hisaab/privacy/
- https://sachin1024-92.github.io/lesster-apps/apps/family-verify/privacy/
- https://sachin1024-92.github.io/lesster-apps/apps/safe-qr/privacy/
- https://sachin1024-92.github.io/lesster-apps/apps/bunk-planner/privacy/

## Status

Policies and store packaging helpers are live. FloatNote (sister app in `daily-motivation-ai`) is the Play pipeline reference: signed AAB from CI, fastlane metadata, UMP consent, supporter tips. Lesster titles reuse that pattern for Play Console closed testing.

## Related

- [FloatNote](https://github.com/sachin1024-92/daily-motivation-ai/tree/main/floating-notepad) — floating notepad template stack
- [ITI Exam Prep](https://github.com/sachin1024-92/itiexamprep-com) — bilingual NCVT CTS prep site
- Profile: [github.com/sachin1024-92](https://github.com/sachin1024-92)
