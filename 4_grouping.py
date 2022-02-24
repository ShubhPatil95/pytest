class TestClass:
    def test_one(self):
            x="Shubham"
            assert "u" in x
    
    def test_two(self):
        x="hello"
        assert hasattr(x,"check")
    
# run command => pytest 4_grouping.py