import os, html
EMAIL="princendlesster@gmail.com"
DATE="17 November 2026"
BASE="/lesster-apps"
CSS="""body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:760px;margin:0 auto;padding:24px 18px;line-height:1.6;color:#1b1b1f;background:#fff}h1{font-size:1.7rem;margin-bottom:.2em}h2{font-size:1.15rem;margin-top:1.6em}a{color:#0b57d0}.muted{color:#5f6368;font-size:.92rem}ul{padding-left:1.2em}.card{border:1px solid #e0e0e0;border-radius:12px;padding:14px 16px;margin:12px 0}.card h3{margin:0 0 4px}footer{margin-top:40px;border-top:1px solid #eee;padding-top:12px;font-size:.88rem;color:#5f6368}"""
ADMOB="""<h2>Advertising (Google AdMob)</h2>
<p>The free version shows ads served by Google AdMob (Google Mobile Ads SDK). To serve and measure ads, Google may collect and process information such as your device's advertising ID, IP address, approximate location derived from IP, app interaction and diagnostic data. This is handled by Google under its own policies: <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from apps that use its services</a> and <a href="https://policies.google.com/privacy">Google Privacy Policy</a>. You can reset or delete your advertising ID, or opt out of personalised ads, in your Android device settings (Settings &gt; Google &gt; Ads, or Settings &gt; Privacy &gt; Ads). Where required, the app asks for your consent before showing personalised ads.</p>"""
BILLING="""<h2>Purchases (Google Play Billing)</h2>
<p>The optional Pro upgrade is sold through Google Play Billing. Payment is processed entirely by Google Play; we never see or store your card, UPI or bank details. We only receive confirmation from Google Play that a purchase is valid so the app can unlock Pro features. See the <a href="https://payments.google.com/payments/apis-secure/u/0/get_legal_document?ldo=0&ldt=privacynotice">Google Payments Privacy Notice</a>.</p>"""
APPS=[
 dict(slug="sahipix",name="SahiPix: Exam Form Photo &amp; Doc Kit",pkg="app.sahipix.formkit",
  blurb="Resize and compress photos, signatures and documents to the exact size and format that exam application forms require.",
  ads=True,
  body="""<h2>What the app does with your files</h2>
<p>SahiPix lets you pick a photo, signature or document from your device (or take one with the camera, if you choose) and converts it to the size, dimensions and file format required by an exam application form. All of this processing happens on your phone. Your photos and documents are <strong>not uploaded</strong> to us or to any server, and we cannot see them.</p>
<p>Files you export are saved only where you choose on your device. Any temporary copies the app makes while editing stay in the app's private storage on your device and are removed when you clear the app's data or uninstall it.</p>
<h2>Permissions</h2>
<ul><li><strong>Camera</strong> (optional): only if you choose to take a new photo inside the app. The image stays on your device.</li><li><strong>Photos / files</strong>: the app uses the Android system picker, so it only gets access to the specific files you select.</li><li><strong>Internet</strong>: used only for ads and Google Play Billing, not to send your files anywhere.</li></ul>"""),
 dict(slug="scam-check",name="Scam Check",pkg="india.scamcheck",
  blurb="Paste or share a suspicious message, link or payment request and get an instant scam risk check in English, Hindi or Hinglish.",
  ads=False,
  body="""<h2>What the app does with your messages</h2>
<p>Scam Check analyses only the text you paste into the app or share to it from another app. The analysis runs on your phone. The app does <strong>not</strong> ask for permission to read your SMS, call log or contacts, and it does not read any message you have not given it yourself.</p>
<p>We do not upload, store or sell the messages you check. Your check history, if the app keeps one, is stored only on your device and is deleted when you clear the app's data or uninstall it.</p>
<h2>Optional link check (Google Safe Browsing)</h2>
<p>If you turn on the optional online link check, web addresses (URLs) found in the message you are checking may be sent to Google's Safe Browsing service so it can tell the app whether the link is known to be dangerous. Only the link is used for this, not the rest of your message. This is handled by Google under the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>. If you leave the online check off, nothing leaves your device.</p>
<h2>Permissions</h2>
<ul><li><strong>Internet</strong>: used only for the optional Safe Browsing link check and Google Play Billing.</li><li>No SMS, call log, contacts, location, camera or microphone permissions are requested.</li></ul>
<p class="muted">Scam Check gives a risk estimate to help you decide. It cannot guarantee that a message is safe. If you have lost money to a cyber fraud in India, call 1930 or report at cybercrime.gov.in.</p>"""),
 dict(slug="vaultmask",name="VaultMask: Private ID Vault",pkg="app.vaultmask.privateid",
  blurb="Keep copies of your ID documents in an encrypted offline vault, mask Aadhaar numbers, and stamp each shared copy with its purpose.",
  ads=False,
  body="""<h2>Your documents stay on your device</h2>
<p>VaultMask is designed to work fully offline. The ID documents and images you add (for example Aadhaar, PAN or other ID cards) are stored <strong>only on your device</strong>, encrypted inside the app's private storage. They are never uploaded to us or to any server, and we have no way to access them.</p>
<p>When you share a document, the app creates a masked copy (for example hiding the first 8 digits of an Aadhaar number) with an optional purpose stamp. The copy goes only to the app or person you pick in the Android share sheet. The share log that records what you shared, when and for what purpose is also stored only on your device.</p>
<h2>Backups and deletion</h2>
<p>Because nothing is stored on our servers, we cannot recover your vault if you lose your phone, forget your lock, or uninstall the app. Uninstalling the app or clearing its data permanently deletes the vault and the share log.</p>
<h2>Permissions</h2>
<ul><li><strong>Camera</strong> (optional): only if you choose to photograph a document inside the app.</li><li><strong>Photos / files</strong>: through the Android system picker, limited to the files you select.</li><li><strong>Biometric / device lock</strong> (optional): used by Android to unlock the vault. Your fingerprint or face data never reaches the app.</li><li><strong>Internet</strong>: used only for Google Play Billing for the Pro upgrade. Your documents are never sent over the internet.</li></ul>"""),
 dict(slug="gig-hisaab",name="Gig Hisaab: Gig Earnings Tracker",pkg="app.gighisaab.ledger",
  blurb="Track delivery and ride-hailing earnings, fuel and expenses, and see your real net pay per hour and per km.",
  ads=False,
  body="""<h2>Your earnings data stays on your device</h2>
<p>Gig Hisaab stores the trips, earnings, fuel and expense entries you add <strong>only on your device</strong>. We do not run a server for this app, and your financial entries are not uploaded to us, shared or sold. The app does not connect to your delivery or ride-hailing accounts and does not read your SMS or bank messages.</p>
<h2>Voice entry</h2>
<p>If you use the optional Hindi or English voice entry, the app uses your phone's built-in Android speech recognition service to turn your speech into text. Depending on your device settings, that service (for example Google's speech service) may process the audio, either on the device or online, under its own privacy policy (<a href="https://policies.google.com/privacy">Google Privacy Policy</a>). The app itself does not record, store or upload your audio; it only receives the resulting text.</p>
<h2>Exports</h2>
<p>If you export a report or backup, the file is created on your device and goes only where you choose to save or share it.</p>
<h2>Permissions</h2>
<ul><li><strong>Microphone</strong> (optional): only when you tap the voice entry button.</li><li><strong>Internet</strong>: used only for Google Play Billing (and for online speech recognition if your device's speech service uses it).</li><li>No location, contacts, SMS or call log permissions are requested.</li></ul>"""),
 dict(slug="family-verify",name="Family Verify",pkg="app.familyverify",
  blurb="A family safe word, a panic script and step-by-step guidance to beat voice-clone, fake emergency and 'digital arrest' scams.",
  ads=False,
  body="""<h2>No personal data collected</h2>
<p>Family Verify works entirely on your device. The safe word, family notes and settings you save are stored <strong>only on your phone</strong>, inside the app's private storage. They are never uploaded to us or anyone else. We do not collect analytics, contacts or any personal information through this app.</p>
<h2>Permissions</h2>
<ul><li>The app requests <strong>no phone permissions</strong>: no contacts, call log, SMS, microphone, camera or location access.</li><li><strong>Internet</strong>: used only for Google Play Billing if you buy the Pro upgrade.</li></ul>
<p class="muted">Family Verify provides general safety guidance and is not legal advice. In India, report cyber fraud by calling 1930 or at cybercrime.gov.in. Police and government agencies never place anyone under "digital arrest" over a video call.</p>"""),
 dict(slug="safe-qr",name="Safe QR &amp; UPI Scanner",pkg="in.successtips.safeqr",
  blurb="Scan any QR code and see where it really leads, who a UPI payment goes to, and whether it shows signs of a scam, before you pay.",
  ads=True,
  body="""<h2>How scanning works</h2>
<p>Safe QR uses your camera to read QR codes. The camera image is processed <strong>on your device</strong> only to decode the QR code; images are not saved or uploaded. The decoded content (for example a link or a UPI payment request) is checked on your device against known scam patterns, such as a "scan to receive money" request or a payee name that does not match.</p>
<p>We do not upload, store or sell the codes you scan. Any scan history is stored only on your device and is deleted when you clear the app's data or uninstall it. The app never makes a payment by itself; if you choose to pay, it hands the request to the UPI app you pick.</p>
<h2>Permissions</h2>
<ul><li><strong>Camera</strong>: to scan QR codes. Used only while the scanner screen is open.</li><li><strong>Photos / files</strong> (optional): through the Android system picker if you choose to scan a QR code from an image.</li><li><strong>Internet</strong>: used for ads and Google Play Billing.</li></ul>"""),
 dict(slug="bunk-planner",name="Attendance &amp; Bunk Planner",pkg="app.bunkplanner.attendance",
  blurb="Track class attendance per subject and see exactly how many classes you can skip while staying above 75%, right on your home screen.",
  ads=False,
  body="""<h2>Your attendance data stays on your device</h2>
<p>Attendance &amp; Bunk Planner stores your subjects, timetable and attendance records <strong>only on your device</strong>. Nothing is uploaded to us or to any server, and we do not collect analytics or personal information. The home-screen widget reads the same data from your device.</p>
<p>Clearing the app's data or uninstalling the app deletes your records. If you export a backup, the file goes only where you choose to save or share it.</p>
<h2>Permissions</h2>
<ul><li><strong>Notifications</strong> (optional): for class or attendance reminders you turn on.</li><li><strong>Internet</strong>: used only for Google Play Billing for the Pro upgrade.</li><li>No location, contacts, camera, microphone or SMS permissions are requested.</li></ul>"""),
]
def page(title, inner):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="robots" content="index,follow"><style>{CSS}</style></head>
<body>{inner}
<footer>Lesster Apps &middot; Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</body></html>
"""
os.makedirs("out/apps", exist_ok=True)
cards="".join(f'<div class="card"><h3>{a["name"]}</h3><p>{a["blurb"]}</p><p class="muted">Package: {a["pkg"]} &middot; <a href="{BASE}/apps/{a["slug"]}/privacy/">Privacy policy</a></p></div>' for a in APPS)
idx=f"""<h1>Lesster Apps</h1><p>Small, privacy-first Android apps for everyday problems in India. Most of our apps work offline and keep your data on your phone.</p>{cards}
<h2>Contact and support</h2><p>Questions, bug reports or data requests: <a href="mailto:{EMAIL}">{EMAIL}</a></p>"""
open("out/apps/index.html","w").write(page("Lesster Apps", idx))
open("out/index.html","w").write(page("Lesster Apps", idx))
for a in APPS:
    common_end = (ADMOB if a["ads"] else "<h2>Advertising and analytics</h2><p>This app does not show ads and does not include advertising or analytics SDKs.</p>") + BILLING + f"""
<h2>Sharing of data</h2><p>We do not sell, rent or share your personal data with anyone. {"Apart from the Google services described above, " if a["ads"] or a["slug"]=="scam-check" or a["slug"]=="gig-hisaab" else ""}the app does not send your data to third parties.</p>
<h2>Security</h2><p>Data the app keeps is stored in the app's private storage on your device, which other apps cannot read. Information sent over the internet (such as Google Play Billing{" and ad requests" if a["ads"] else ""}) uses encrypted HTTPS connections.</p>
<h2>Data retention and deletion</h2><p>Because your data is kept on your device, you control it. You can delete it at any time from within the app where available, by clearing the app's storage in Android Settings, or by uninstalling the app. We hold no copy of it on our side, so there is nothing for us to delete; you can still email us with any privacy request and we will reply within 30 days.</p>
<h2>Children</h2><p>This app is not directed at children under 13, and we do not knowingly collect personal information from children.</p>
<h2>Changes to this policy</h2><p>If we change this policy, we will update this page and the "Last updated" date below. Material changes will also be noted in the app's Google Play listing.</p>
<h2>Contact</h2><p>Developer: Lesster<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p class="muted">Last updated: {DATE}</p>"""
    inner=f"""<p class="muted"><a href="{BASE}/">&larr; Lesster Apps</a></p><h1>Privacy Policy: {a["name"]}</h1>
<p class="muted">Android app package: {a["pkg"]} &middot; Developer: Lesster</p>
<p>This policy explains what information the {a["name"]} app ("the app") handles, and how. In short: <strong>we do not collect your personal data on our servers.</strong> {"The free version shows Google AdMob ads, described below." if a["ads"] else ""}</p>
{a["body"]}{common_end}"""
    os.makedirs(f"out/apps/{a['slug']}/privacy", exist_ok=True)
    open(f"out/apps/{a['slug']}/privacy/index.html","w").write(page(f"Privacy Policy - {html.unescape(a['name'])}", inner))
print("ok")
