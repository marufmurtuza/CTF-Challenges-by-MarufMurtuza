Challenge Name: Find The Hacker 2

Challenge Category: OSINT

Challenge Flag: `KCTF{46.7547448,7.6303549}`

Description: 

Hey hacker,
Thanks for helping us last time. But unfortunately we failed to capture the hacker. Because the hacker left the place before the police reached there. 
But the hacker left a trace for us. When we raided the place where he was living in Lala Khal, we found a cellphone in the trash bin.
Though the hacker tried to destroyed it, but the police forensic team managed to recover the phone.
After recovering the phone, police found that, the hacker sent a picture attached email to someone with a temp email.
And in the email, he worte that,
"Meet me in the place where we met for the first time, hope you recognize the place from the photo."

Can you help us to find the location?

Flag Format: KCTF{xx.xxxxxxx,x.xxxxxxx}

Solution: 

In the Image there is a qr code. But the QR code needs some fixing. After fixing the QR code, it will lead to a table booking site.
In that site, the solvers will find the restaurant name "Mani’s coffee & bagels"
So, they need to google search that name. and google map will give them the co-ordinates.
