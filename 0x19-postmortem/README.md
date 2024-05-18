### Project postmortem

`project url` : [loadshedding]<https://github.com/Koketso-dax/loadshedding.git>

#### Issue Summary:

- Project was built on undocumented public api available to but not openly maintained for developers.

- The Api has been down and modified a number of times causing the app to stop working.

- This affected all users of the api even outside my application.

#### timeline:

- Issues where first detected by myself (the developer) and other developers online.

- The app has been temporarily taken down and will be fixed in later versions.

- Initially I thought the api was permanetly taken down there was no way of knwing since it is not maintained however upon a few tests being run it was discovered the api routes had been changed.

- An announcement was written on git to inform users the app is down.

#### Root cause:

- Issue was cause by undocumented, unmaintained API.

- Might be resolved by creating the API from scratch however it is not easy to manually fetch and serve the data.

#### Corrective measures:

- The API will be investigated and manually documented.

- A backup will be created and deployed incase of changes in the future ect.