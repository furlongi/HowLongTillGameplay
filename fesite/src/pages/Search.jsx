import React, {useState, useEffect} from "react";
import Query from "../service/Query";


const Search = ({history, location, match}) => {
    const [isLoading, setLoading] = useState(true);
    const [results, setResults] = useState();

    useEffect(() => {
        Query.search(window.location.search)
            .then(response => {
                setResults(response.data); 
                // Remember results are encapsulated by another 'data'
                setLoading(false);
            })
            .catch(response => 
                {
                    console.log(response);
                }
        ); // Replace catch later
    }, []);

    return ( isLoading ? (<h1>Loading...</h1>) : (
        <div className="form-search">
            <div className="form-items">
            </div>
            <h1>Search</h1>
        </div>
        )
    );
}

export default Search;