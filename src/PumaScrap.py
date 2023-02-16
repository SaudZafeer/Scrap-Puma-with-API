import requests
import pandas as pd

def PumaApi():
  apppended = []
  csv = pd.read_csv(r'D:\Saud\PumaScrap\Puma API\Input\Puma_Style.csv')
  csv_data = csv['style']
  print(csv_data)
  for styles in csv_data:
    try:
      url = "https://us.puma.com/api/graphql"

      payload = {
          "query": '''query ProductSearch($q: String, $sort: String, $filters: [FilterInputOption!]!, $expansions: [ProductSearchExpansion!], $includeSearchMetadata: Boolean = true, $offset: Int!, $limit: Int!) {
        search(
          input: {q: $q, sort: $sort, filters: $filters, limit: $limit, offset: $offset, expansions: $expansions, includeSearchMetadata: $includeSearchMetadata}
        ) {
          __typename
          ...PaginatedOutputNodesFragment
          ...PaginatedOutputMetadataFragment @include(if: $includeSearchMetadata)
        }
      }

      fragment PaginatedOutputNodesFragment on PaginatedOutput {
        nodes {
          __typename
          id
          color
          masterId
          variantProduct {
            ...mandatoryVariantFields
            badges {
              id
              label
              __typename
            }
            percentageDiscountBadge
            salePrice
            productPrice {
              price
              salePrice
              promotionPrice
              __typename
            }
            displayOutOfStock {
              soldout
              comingsoon
              backsoon
              presale
              displayValue
              __typename
            }
            orderable
            promotions(page: ProductListingPage) {
              id
              calloutMessage
              __typename
            }
            __typename
          }
          masterProduct {
            ...mandatoryMasterFields
            brand
            promotions(page: ProductListingPage) {
              id
              calloutMessage
              __typename
            }
            score {
              rating
              amount
              __typename
            }
            __typename
          }
        }
      }

      fragment PaginatedOutputMetadataFragment on PaginatedOutput {
        sortingOptions {
          id
          label
          __typename
        }
        selectedSort
        filteringOptions {
          id
          label
          values {
            value
            label
            hitCount
            __typename
          }
          __typename
        }
        totalCount
      }

      fragment mandatoryMasterFields on Product {
        name
        id
        orderableColorCount
        displayOutOfStock {
          soldout
          soldoutWithRecommender
          comingsoon
          backsoon
          presale
          displayValue
          __typename
        }
        colors {
          name
          value
          image {
            href
            __typename
          }
          __typename
        }
        image {
          href
          alt
          __typename
        }
      }

      fragment mandatoryVariantFields on Variant {
        id
        masterId
        variantId
        name
        price
        colorValue
        colorName
        sizeGroups {
          label
          description
          sizes {
            id
            label
            value
            productId
            orderable
            maxOrderableQuantity
            __typename
          }
          __typename
        }
        preview
        images {
          alt
          href
          __typename
        }
      }
      ''',
          "operationName": "ProductSearch",
          "variables": {
              "q": styles,
              "filters": [],
              "includeSearchMetadata": False,
              "offset": 0,
              "limit": 24
          }
      }
      #Add Your Headers for authorization
      headers = {
    
}
      response = requests.request("POST", url, json=payload, headers=headers)
      data = response.json()['data']['search']['nodes']
      for item in data:
          id = item['variantProduct']['id']
          name = item['variantProduct']['name']
          price = item['variantProduct']['price']
          preview = item['variantProduct']['preview']
          print(preview,id,name,price)
          try:
            salePrice = item['variantProduct']['salePrice']
            print(salePrice)
            data = {
              'Image': preview,
              'id': id,
              'Name': name,
              "price": price,
              "Sale": salePrice
            }
            apppended.append(data)
          except:
              print('no sale price available')
              data = {
              'Image': preview,
              'id': id,
              'Name': name,
              "price": price,
              "Sale": "NA"
              }
              apppended.append(data)
    except:
      print("product might not be available...\nor most probably headers are expired...")
  df = pd.DataFrame(apppended)
  df.to_csv(r'D:\Saud\PumaScrap\Puma API\Result\Puma data.csv',index=False)
PumaApi()
