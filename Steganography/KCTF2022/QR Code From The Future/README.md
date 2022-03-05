Challenge Name: QR Code From The Future

Challenge Category: Steganography

Challenge Difficulty: Medium

Challenge Flag: `KCTF{QR_code_got_evolved_from_static_to_dynamic}`

Challenge Author: marufmurtuza

<h1>Description:</h1>
The following file was found in a device from a crashed UFO. Can you solve that mystery?

Flag Example: `KCTF{SOME_text_here}`



<h1>Challenge Solution:</h1>

I've provided a sample python script with the challenge. You can run that script to see how it's gonna work.
Don't forget to keep the script and the gif in the same folder while running the script.

Required Modules for my script:

- `pyzbar`
- `pillow`
- `Images`

Players need to write a script to extract the letters from the gif.

They will get a Mirrored ROT13 Flag.

Mirrored Rot13 Flag: `}pvznalq_bg_pvgngf_zbes_qriybir_gbt_rqbp_ED{SGPX`

So, they need to shift that mirrored rot13 flag.

After shifting they Original flag will be revealed in a mirrored pattern.

Mirrored FLag: `}cimanyd_ot_citats_morf_devlove_tog_edoc_RQ{FTCK`

So, they need to reverse print the mirrored flag to get the original flag.
