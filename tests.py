import glob
import unittest
import frontmatter

class TestPosts(unittest.TestCase):
    REQUIRED_KEYS = [
        "title",
        "description"
    ]

    def test_posts(self):
        tags = []
        for file in glob.glob("_posts/*.md"):
            # Skip drafts
            if file.startswith("_posts/_"):
                continue

            with open(file) as f:
                post = frontmatter.load(f)

            for key in self.REQUIRED_KEYS:
                if key not in post:
                    self.fail(
                        f"La clé `{key}` est absente de `{file}` et est obligatoire"
                    )

            image = post["image"]
            if not (image.startswith("/img/") or image.startswith("http")):
                self.fail(f"L'image de `{file}` semble invalide : {post['image']}")

            self.assertEquals(post["layout"], "post")


class TestPodcastPosts(unittest.TestCase):
    REQUIRED_KEYS = [
        "title",
        "description",
        "date",
        "file",
        "duration",
        "guid",
        "spotify_url",
        "itunes_url",
        "description",
        "image"
    ]

    def test_podcast_posts(self):
        tags = []
        for file in glob.glob("_hackerspublics/*.md"):

            with open(file) as f:
                post = frontmatter.load(f)

            for key in self.REQUIRED_KEYS:
                if key not in post:
                    self.fail(
                        f"La clé `{key}` est absente de `{file}` et est obligatoire"
                    )

            image = post["image"]
            if not (image.startswith("/img/") or image.startswith("http")):
                self.fail(f"L'image de `{file}` semble invalide : {post['image']}")

            self.assertEquals(post["layout"], "episode")
