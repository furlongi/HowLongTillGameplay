import React from "react"
import { Switch, Route } from "react-router-dom"
import Home from "../pages/Home"
import Search from "../pages/Search"

const Content = () => {
    return (
        <div className="content">
            <Switch>
                <Route path="/search"
                       component={props => < Search{...props} />}
                />
                <Route path="/search?:name"
                       component={props => < Search{...props} />}
                />
                <Route path="/"
                       component={props => < Home{...props} />}
                />
                {/* <Route path="*"
                       component={props => < Home{...props} />}
                /> */}
            </Switch>
        </div>
    )
}

export default Content;