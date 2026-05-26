# Publishing Checklist

Use this checklist before making the repository public.

- [x] Add exported PDF slides to `slides/`.
- [x] Add optional PPTX deck to `slides/`.
- [ ] Confirm `assets/finbot-architecture.png` is the latest architecture diagram.
- [ ] Confirm `assets/finbot-observability-results.png` is the latest benchmark/results diagram.
- [ ] Confirm all screenshots blur project IDs, billing account IDs and private data.
- [ ] Confirm README prerequisites match the final demo setup.
- [ ] Replace placeholder GitHub URLs in `README.md`.
- [ ] Review `toolbox/tools.example.yaml` and keep only safe sample SQL.
- [ ] Review `docs/mcp-client-integration.md` and replace placeholder Cloud Run URLs if publishing a live endpoint.
- [ ] Review `docs/references.md` and confirm all links are still relevant.
- [ ] Decide whether `demos/finops-cloud-agent` should remain runnable or code-reference only.
- [ ] Confirm no `.env`, credential files, deployment metadata or local virtualenv files are present.
- [ ] Create the GitHub repository.
- [ ] Push the first commit.
- [ ] Create a GitHub release with the final PDF and optional PPTX.
