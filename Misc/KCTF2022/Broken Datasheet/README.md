Challenge Name: Broken Datasheet

Challenge Category: Misc

Challenge Flag: `KCTF{XLSX_Fil3$_4R3_Actually_0n3_Kind_0f_Zip_Fil3}`

Description: 

One of my friend sent me an important datasheet to me.
But the sheet seems broken.
Can you please help me to recover or read the datasheet.

Solution:

XLSX are actually one kind of zip file. In the main file there is no text in it.
But if the solvers open the XLSX file in a zip manager, they will find another datasheet inside it.
In that datasheet, In "KCTx2022" They will find the flag.