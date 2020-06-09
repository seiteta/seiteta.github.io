module.exports = {
  ci: {
    collect: {
      staticDistDir: ['/home/runner/work/seiteta.github.io/seiteta.github.io']
    },
    assert: {
      assertions: {
        "categories:accessibility": ["warn", {"minScore": 1}],
        "categories:accessibility": ["error", {"minScore": 0.8}]
      },
    },
  },
};
