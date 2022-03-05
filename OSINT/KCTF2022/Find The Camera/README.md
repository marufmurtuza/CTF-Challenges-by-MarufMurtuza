Challenge Name: Find The Camera
Difficulty: ...
Category: OSINT
Author: marufmurtuza

Flag: `KCTF{SONY_DSC_S980}`

<h1>Description:</h1>
Can you find the manufacturer and the model number of the camera that took the picture of this bus?

Note: The whole flag is in Upper Case letters and replace any special character or space with underscores.

Flag format is: `KCTF{MANUFACTURER_MODEL_SINGLELETTER&NUMBER}`


<h1>Solve:</h1>

Solvers may search the picture on Google. But that will not help them at all.
But there is Copyright Symbol of the photographer in the image.
So, if they search on google the name of that photographer and the Number Plate of the car like that "JenCh012 QV6227",
then google will give the following link.

`https://fotobus.msk.ru/vehicle/204172/?lang=en`

And from that link, they will get the image. If they click on the image, they will be redirected to;
`https://fotobus.msk.ru/photo/267442/?vid=204172`

And here they will find all the details.

Note: They won't be able to extract any information from the given file because,
I took a screen-shot and giving it here rather than downloading the original photo.
