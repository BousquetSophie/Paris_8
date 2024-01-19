let cnv = document.getElementById('myCanvas');
let ctx = cnv.getContext('2d');
ctx.imageSmoothingEnabled= false;

let img_names = ["civil1","civil2",
"civil3", "civil4", "civil5", "civil6", "civil7", "civil8", "civil9", "civil10", "civil11", "civil12", "civil13", "civil14"];
let all_img = [];

for(let i = 0; i < 14; i += 1)
{
    let img = new Image();
    img.src = "./assets/"+img_names[i]+".png";
    all_img.push(img);
}

let decale_droite = 10
let decale_bas = 10

function update()
{
    for(let k = 0; k < 7; k += 1)
    {
        ctx.drawImage(all_img[k], decale_droite, decale_bas, 125, 250);
        decale_droite += 135 
    }

    decale_droite = 10
    decale_bas = 270

    for(let j = 7; j < 14; j += 1)
    {
        ctx.drawImage(all_img[j], decale_droite, decale_bas, 125, 250);
        decale_droite += 135 
    }
}
setInterval(update, 200);