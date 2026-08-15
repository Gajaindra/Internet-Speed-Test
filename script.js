async function speedCheck() {
    const button = document.getElementById("testButton");
    const download = document.getElementById("download");
    const upload = document.getElementById("upload");
    const ping = document.getElementById("ping");
    const status = document.getElementById("status");

    button.disabled = true;

    download.innerHTML = "--";
    upload.innerHTML = "--";
    ping.innerHTML = "--";

    status.innerHTML = "Testing...";
    status.style.color = "orange";

    try {
        const response = await fetch("/speedtest");
        const data = await response.json();

        if (data.success) {
            download.innerHTML = data.download.toFixed(2);
            upload.innerHTML = data.upload.toFixed(2);
            ping.innerHTML = data.ping.toFixed(2);

            status.innerHTML = "Test completed";
            status.style.color = "green";
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error(error);

        status.innerHTML = "Speed test failed";
        status.style.color = "red";

        download.innerHTML = "--";
        upload.innerHTML = "--";
        ping.innerHTML = "--";
    }

    button.disabled = false;
}
