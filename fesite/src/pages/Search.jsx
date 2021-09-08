import React, {useState, useEffect} from "react";
import Query from "../service/Query";
import BoxColorInfo from "../items/gameBoxColor";


const Search = ({history, location, match}) => {
    const [isLoading, setLoading] = useState(true);
    const [results, setResults] = useState();
    console.log("match", match);

    useEffect(() => {
        Query.search(window.location.search)
            .then(response => {
                setResults(response?.data?.data);
                console.log(response?.data?.data);
                setLoading(false);
            })
            .catch(response => 
                {
                    console.log(response);
                }
        ); // Replace catch later
    }, [match.params.name]);

    const buildList = () => {
        if (results == null) {
            return (<h1>No games found.</h1>);
        }
        return (
            <ul className="list-unstyled card-columns">
                {results.map((entry) => {
                    let gameUrl = `game?id=${entry["id"]}`;

                    return (
                        <li className="box-style">
                            <div>
                                <a href={gameUrl}>
                                    <img alt="Game Box Art" src={entry["cover"]}/>
                                </a>
                            </div>
                            <div className="game-info">
                                <h3 className="game-title">
                                    <a href={gameUrl}>
                                        {entry["name"]}
                                    </a>
                                </h3>
                                {BoxColorInfo.colorBox(BoxColorInfo.timeFormat, entry["time"])}
                            </div>
                        </li>
                    )}
                )}
            </ul>
        );
    }

    return ( isLoading ? (<h1>Loading...</h1>) : (
        <div className="form-search">
            <div className="form-items">
            </div>
            <h1>Search</h1>
            {buildList()}
        </div>
        )
    );
}

export default Search;