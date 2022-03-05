Challenge Name: Obsfuscation Isn't Enough

Challenge Category: Web

Challenge Difficulty: Beginner Friendly

Challenge Author: marufmurtuza

Challenge Flag: `KCTF{0bfuscat3d_J4v4Scr1pt_aka_JSFuck}`

<h1>Description:</h1>
One of my friend developed this login panel and dared me to get the flag by logging in.
I tired to bruteforce the login panel.
But it doesn't work at all.
Can you please figure out the login credentials or something more valuable for me?

`http://<ip>:20001`

<h1>Setup:</h1>

```shell
docker-compose up
```

<h1>Solution:</h1>

In the source-code, the solvers will find a JSFuck.
After decoding the JSFuck, they will find the following code.

```
if (document.forms[0].username.value == "83fe2a837a4d4eec61bd47368d86afd6" && document.forms[0].password.value == "a3fa67479e47116a4d6439120400b057") document.location = "150484514b6eeb1d99da836d95f6671d.php"
```

In this code, we can see that the name of our flag file is `150484514b6eeb1d99da836d95f6671d.php`

So, solver needs to visit `http://<ip>:20001/150484514b6eeb1d99da836d95f6671d.php` to get the flag.

