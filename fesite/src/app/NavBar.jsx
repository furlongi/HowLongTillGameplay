import React, { useState } from "react"
import { useHistory } from "react-router-dom"
import { Navbar, Nav, Form, FormControl } from "react-bootstrap";

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
