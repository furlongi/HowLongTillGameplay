import React, { useState } from "react"
import { Switch, Route, useHistory } from "react-router-dom"
import { Navbar, Nav, Form, FormControl, Button, NavDropdown, Container } from "react-bootstrap";

const NavBar = () => {
  const [gameName, setGameName] = useState(null);
  const history = useHistory();

  const handleSearch = (e) => {
    e.preventDefault();
    if (gameName == null) {
      history.push({pathname:`/search`});
    } else {
      history.push({pathname:`/search?name=${gameName}`});
    }
  }

  return (
      <Navbar className="nav-bar" expand="lg">
          <Form inline className="form-search-on-nav" onSubmit={handleSearch}>
            <FormControl
              type="search"
              placeholder="Search a game..."
              onChange={(e) => setGameName(e.target.value)}
              className="me-sm-2 nav-search"
            />
          </Form>

          <Nav.Link onClick={handleSearch}>Search</Nav.Link>
          <Nav.Link href="/submit">Submit</Nav.Link>

          <div className="ms-auto">
            <Nav.Link href="/about">About</Nav.Link>
          </div>

      </Navbar>
  )
}

export default NavBar;
        // <nav className="nav-bar">
        //     <div>
        //         <input type="text" />
        //     <NavLink className="nav-button" to="/search">
        //         Search
        //     </NavLink>
        //     </div>
        //     <NavLink className="nav-button" to="/about">
        //         About
        //     </NavLink>
        // </nav>

        /* <nav class="navbar navbar-expand-lg navbar-light nav-bar">
  <div class="container-fluid">

    <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
        <button class="btn btn-outline-success" type="submit">Search</button>
    </form>


    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></hr></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
</nav> */