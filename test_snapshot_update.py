import snapshottest

class UpdateTest(snapshottest.TestCase):
    def test_snapshot(self):
        self.assertMatchSnapshot({
            "foo": 42,
            "bar": 123,
        })
