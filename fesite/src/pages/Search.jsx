import React, {useState} from "react";
import { useParams } from "react-router-dom";
import Query from "../service/Query";

const Search = ({history, location, match}) => {
    const {name} = useParams();
    console.log(location.search);
    console.log(name);
    console.log(match.params);

    Query.search("?name=xeno")
         .then(response => {})
         .catch(response => {console.log(response);});

    return (
        <div className="form-search">
            <div className="form-items">

            </div>
            <h1>Search</h1>
        </div>
    );
}

export default Search;