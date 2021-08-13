import Axios from "axios"

async function sendHttp(method, props) {
    const options = {
        ...props,
        method: method
    };

    return Axios.request(options)
}

async function GET(props) {
    return await sendHttp("GET", props);
}

async function POST(props) {
    return await sendHttp("POST", props);
}

const Socket = {
    GET,
    POST,
};

export default Socket;