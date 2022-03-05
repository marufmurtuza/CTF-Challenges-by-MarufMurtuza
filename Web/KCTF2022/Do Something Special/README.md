Challenge Name: Do Something Special

Challenge Category: Web

Challenge Difficulty: Beginner Friendly

Flag: `KCTF{Sp3cial_characters_need_t0_get_Url_enc0ded}`

Author: marufmurtuza

<h1>Description:</h1>

Alex is trying to get the flag from this website.
But something is wrong with the button.
Can you help him to get the flag?

`http://<IP>:20000`

<h1>Docker Setup</h1>

```shell
docker-compose up
```

<h1>Solution:</h1>

From the source code, solvers will get to know the file name `gr@b_y#ur_fl@g_h3r3!`.

But it won't work until it gets url encoded.

So, solvers need to url encode the file name and then they will get something like this `http://<IP>:20000/gr%40b_y%23ur_fl%40g_h3r3!`

And that will give them the flag.



