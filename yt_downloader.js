const readline = require('readline');
const ytdl = require('ytdl-core');
const ffmpeg = require('fluent-ffmpeg');


const downloadVideo = async (link) => {
    let title;
    let stream = ytdl(link, {
    quality: 'highestaudio',
    });
    await stream.on('info', (info) => {
        title = info['videoDetails']['title'];
        let start = Date.now();
        ffmpeg(stream)
        .audioBitrate(128)
        .save(`${__dirname}/${title.replace(/[^a-zA-Z ]/g, "")}.mp3`)
        .on('progress', p => {
            readline.cursorTo(process.stdout, 0);
            process.stdout.write(`${p.targetSize}kb downloaded`);
        })
        .on('end', () => {
            console.log(`\ndone, thanks - ${(Date.now() - start) / 1000}s`);
        });
    })

}

downloadVideo("https://youtu.be/ZRtdQ81jPUQ");