# python serverless

documentation: <https://documenter.getpostman.com/view/3827865/TW6xoofc>

api url: <https://lh0hgo3pqg.execute-api.ap-southeast-1.amazonaws.com/prod/>

## Requirement

- install python (v3.8)
- install yarn
- install node (v14+)
- install serverless

## Testing and run

```zsh
// install node dependencies
$ yarn

// install python dependencies
$ pip3 install -r requirements.txt

// test api in local
$ yarn run dev

// deploy to serverless
$ yarn run deploy

// open serverless dashboard
$ yarn run dashboard

// remove serverless services in aws (api gateway, lambda, s3, cloudformation)
$ yarn run remove
```
