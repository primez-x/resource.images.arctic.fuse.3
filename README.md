# Arctic Fuse 3 Image Resources

This Kodi resource add-on packages images used by Arctic Fuse 3. Primez maintains the package, which credits the original Arctic Fuse 3 image work to jurialmunkey.

## Install

1. Install the [Primez repository ZIP](https://primez-x.github.io/kodi.addons/repository.primez.addons/repository.primez.addons-1.0.0.zip) in Kodi with **Install from zip file**.
2. Install **Arctic Fuse 3** from the Primez repository.

The skin declares `resource.images.arctic.fuse.3` as a dependency. Kodi installs the image package with the skin.

## Use

The package registers Kodi image resource type `arctic.fuse.3`. Skin XML and shortcuts load images from this URI prefix:

```text
resource://resource.images.arctic.fuse.3/extras/
```

The source contains image assets, metadata, and tests. The package has no Python service or settings entry point; install Arctic Fuse 3 to use the images through the skin.

## Source layout

- `resources/extras/backgrounds/` — backgrounds, seasonal images, overlays, and launch artwork.
- `resources/extras/icons/` — interface and metadata icons.
- `resources/extras/modes/` — mode artwork.
- `resources/extras/profiles/` — profile images.
- `resources/extras/screenshots/` — add-on screenshots.
- `resources/extras/viewtypes/` — view preview images.
- `addon.xml` — Kodi resource registration and image metadata.
- `tests/` — resource manifest and asset checks.

## Maintenance

The tracked branch is `main`. Run the configured check from the repository root:

```sh
python3 -m unittest discover -s tests
```

Enable the local pre-push checks with:

```sh
git config core.hooksPath .githooks
```

For changes to shipped behavior, update the root `addon.xml` version and add the matching `<news>` entry. README-only edits need no version bump. Follow the central [versioning policy](https://github.com/primez-x/kodi.addons/blob/main/VERSIONING.md). The central [repository guide](https://github.com/primez-x/kodi.addons/blob/main/README.md) documents the source webhook and GitHub Actions publish flow.

## Credit and license

The image library credits [jurialmunkey](https://github.com/jurialmunkey). Primez maintains this fork. The package uses the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license](LICENSE.txt).
