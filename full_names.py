def make_full_name(family_name, given_name):
    """Return the full name, neatly formatted."""
    full_name = f"{family_name} {given_name}"
    return full_name.title()

def extract_family_name(full_name):
    """Return the family name from a full name."""
    family_name = full_name.split(" ")[0]
    return family_name

def extract_given_name(full_name):
    """Return the given name from a full name."""
    given_name = full_name.split(" ")[1]
    return given_name


from pytest import approx
import pytest
# Test the functions
def test_make_full_name():
    """Test the make_full_name function."""
    assert make_full_name("Doe", "John") == "Doe John"
    assert make_full_name("Smith", "Jane") == "Smith Jane"
    assert make_full_name("Toussaint", "Marie") == "Toussaint Marie"
    assert make_full_name("Toussaint", "Oliver") == "Toussaint Oliver"
    assert make_full_name("Washington", "George") == "Washington George"
    assert make_full_name("Washinton", "Martha") == "Washinton Martha"
    
def test_extract_family_name():
    """Test the extract_family_name function."""
    assert extract_family_name("Toussaint Marie") == "Toussaint"
    assert extract_family_name("Toussaint Oliver") == "Toussaint"
    assert extract_family_name("Washington George") == "Washington"
    assert extract_family_name("Washinton Martha") == "Washinton"

def test_extract_given_name():
    """Test the extract_given_name function."""
    assert extract_given_name("Toussaint Marie") == "Marie"
    assert extract_given_name("Toussaint Oliver") == "Oliver"
    assert extract_given_name("Washington George") == "George"
    assert extract_given_name("Washinton Martha") == "Martha"

pytest.main(["-v", "--tb=line", "-rN", __file__])