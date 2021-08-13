import Socket from "./Socket";
import { baseUrl, searchEP } from "../config/config.json";

async function search(query) {
    const props = {
        baseURL: baseUrl,
        url: searchEP.search + query
    };

    return Socket.GET(props);
}

const Query = {
    search
};

export default Query;