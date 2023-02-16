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
      headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept": "application/graphql+json, application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://us.puma.com/us/en/search?q=531857_74",
    "content-type": "application/json",
    "locale": "en-US",
    "bloomreach-id": "uid=3596857681154:v=12.0:ts=1676569409059:hc=9",
    "puma-request-source": "web",
    "x-operation-name": "ProductSearch",
    "authorization": "Bearer eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmNqcF9wcmQiLCJraWQiOiIwNmUwYjljOC1iZjA3LTRjNDUtYTQ2OC05MDA3Mjk2NzI3ZjUiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzIHNmY2Muc2hvcHBlci1wcm9kdWN0cyBzZmNjLnNob3BwZXItbXlhY2NvdW50LnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMubG9naW4gc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5vcmRlcnMgc2ZjYy5zaG9wcGVyLWN1c3RvbWVycy5yZWdpc3RlciBzZmNjLnNob3BwZXItYmFza2V0cy1vcmRlcnMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5hZGRyZXNzZXMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMucncgc2ZjYy5zaG9wcGVyLXByb2R1Y3RsaXN0cyBzZmNjLnNob3BwZXItcHJvbW90aW9ucyBzZmNjLnNob3BwZXItYmFza2V0cy1vcmRlcnMucncgc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wYXltZW50aW5zdHJ1bWVudHMucncgc2ZjYy5zaG9wcGVyLWdpZnQtY2VydGlmaWNhdGVzIHNmY2Muc2hvcHBlci1wcm9kdWN0LXNlYXJjaCBzZmNjLnNob3BwZXItbXlhY2NvdW50LnByb2R1Y3RsaXN0cyBzZmNjLnNob3BwZXItY2F0ZWdvcmllcyBzZmNjLnNob3BwZXItbXlhY2NvdW50Iiwic3ViIjoiY2Mtc2xhczo6YmNqcF9wcmQ6OnNjaWQ6MWM4YzhhM2UtNjU2ZS00MWIxLThiNmYtZmIwNmM0NTFmMDE5Ojp1c2lkOmQwMWUxMjg2LWEzMTAtNDhiYi1hZTVlLTA3N2E4YjBjMzA5NSIsImN0eCI6InNsYXMiLCJpc3MiOiJzbGFzL3Byb2QvYmNqcF9wcmQiLCJpc3QiOjEsImF1ZCI6ImNvbW1lcmNlY2xvdWQvcHJvZC9iY2pwX3ByZCIsIm5iZiI6MTY3NjU4MTU3Mywic3R5IjoiVXNlciIsImlzYiI6InVpZG86c2xhczo6dXBuOkd1ZXN0Ojp1aWRuOkd1ZXN0IFVzZXI6OmdjaWQ6YmZ4Y2FWeHJkV21jd1J3cmtWa2JZWW1laEc6OmNoaWQ6TkEiLCJleHAiOjE2NzY1ODM0MDMsImlhdCI6MTY3NjU4MTYwMywianRpIjoiQzJDLTE4NDQ2MDQ3NzAwNzQwNjM0MzcyNTUzMTM0OTA5NDg3Mjk5In0.n_O14B7UtEZfgIV7lU1Gmenx-_cVFaPGjPct61GmVg_ZVscefWIpQM_E82j-vswMlyRKueBpd5D1J2rftb-BaQ",
    "refresh-token": "32vJI68OGWrTTQmVIfUHyIH5Hj9T06z3vJ27MC04E3s",
    "customer-id": "bfxcaVxrdWmcwRwrkVkbYYmehG",
    "customer-group": "f98875ac004d61701f47f669c8bb3d79f63b23dc454f93658851cc846fa2bed9",
    "hpm0vOKCHE-f": "A5K5DlyGAQAAuswk6hh9YFjmZm0EdTyUv1p5RaCanWMfP9NIKGh6LwniP_o7Abm783OcuOFZwH8AAEB3AAAAAA==",
    "hpm0vOKCHE-b": "-15jb79",
    "hpm0vOKCHE-c": "AGB0C1yGAQAA-aaShNoT8le4DrWtlmOD4rRrxNZHIWwo7_G3SxEuurlsdMT4",
    "hpm0vOKCHE-d": "ABaChIjBDKGNgUGAQZIQhISi0eIApJmBDgARLrq5bHTE-AAAAAAyc2D1AFdhFnP07sj9i9vJaXSxNS0",
    "hpm0vOKCHE-z": "q",
    "hpm0vOKCHE-a": "LLTG=B3nA9r0t6cFjuxbWmAC9bgzFIkQvmbwLkTkWin-RS63YmVtrbcvmd5HJJMGwYfHjNJgwqnfllVD6_B=OHR=jFMpNLTu0ccjWcP0C2pU5HUm9lQVX_3Ml84QwK6gF3MK30iN_Jwnzz9WQ5s--qJaNAPX6Ga=i9vYV=K5CgEdSj1Yn_sxJ65BWlf72lnPvpV4Znaum_8l4-R0AoXzh=HsrOzwGkBkLIAqM1u5spP=8CrNq378pA8PFWc89TVlLF16roM6x2pjwd1vY0pAL5U=kjPQ76XTpH7INUsGLtEKhG_CWpg2r9ZaEcF9OHvWUogHz4ruBXRDDXlB1JMGcuxsgSpsuc-DLp71WaJSHFZGktHpraN4IgOA0kHdX5ySXwif2L_x3ZObhGG8tNBi5vqQhCvlyQnIwiqxR1XnlpYZH7-FW1j2cu5xpslzZspFFHvGLIg7qBEyEJudpWFtP1FcuOBuiwS=IZ=c_=SDz-5s3MVg2JYltR0U0KkdGnsGaiF_71Et7DQlCvDHp-ShwV6DYLI1w49p7vbdff9yTsBMp59txjOPbmrPrS7D8IIqSN3DUSKB5KIn=xM4VgtK6j5diL3kxTXu3qtRiL0XyOq3x-3q-02Pgk8D15pVJZWGp_QoP7Gy6Az0VX7uWBZit38vb5OPovm7SXK-Zc5X-huhUCbT563=hbA6lcWZdA6wk=AGrqK2i7bkTWGm9iGpPUcSE3Jj777jZX=Pm=sGIBSMjKHqCwHNGmZ6ayzQYGF63cI3RuY82RFD2vpf_NTdMkWBgS9jsDko-CD0EU5kPlbmbnXGob2J=aT7LAsya_5JmTdrPBJlmz8Tsj6n4DPD3R7Ww7QgZl_iRnEOfmzqVvR4A9BxXCnGsF8sl_bO1XODb4SYc_c75Q3AHYgE6IdvSDAnXQATk3zstvaLruuUmWFb03mdtSwhxF0Ahm=fKh7TK63wfBcKFN-oDJf4fUhpoS6zA7hZAiq4EkBHR2VEO--RCMr_=-nW_QEGL9thpd-K5r4=8QyK9aGEUfNdWFQBDxOTN_Wy-gmJq6SyRzuAbUEiCcdZIfyx5kRS94jDDdEW7jxDAryTE5nR1hlgk8QBDzMPH9b7npXTACNm8jiRgYD6K=7mLY=K0613j9nwhs8Xg1inoS3XJ7bKGWXEOCNfT0mJz-Hxbnp3pdBFEbZvzKQCZdfNrFd1jf0A=-fbln9FgUqvd-BEAVy=H=Q-7_HEG_M8A-8v41RCf=bh3DsccsoCcGLjzrtpcXtWd0-oQ2ENUMfSZD1xhDUKIBQiIIWJqtYUkAgvx8y3lFUaL=qMhjYahmgWmu_QfX_07c=QJ8yR--8cIHg=NB98l7xdNB=dAR3thAZj1RoJSFhB1kNNz7hrZApocdilh1UwJEKHHWjrTHl_RJYn5suAYK8hbsLmasgQA2fBFf44UBUKqxljmDn-qDAkNHgyqqYaAN=PDMF=FXg-jz=FDSvH",
    "Origin": "https://us.puma.com",
    "Connection": "keep-alive",
    "Cookie": "Ldl7YnFK=AwzqUluGAQAAtjbPlvcdHzefjahoVNeSmhVrLiGU16qjGglXdUn6lufAFQT0Abm783OcuOFZwH8AAEB3AAAAAA|1|0|24c9efebe84381ee1aae256a6c072bcc5ba34b79; __gtm_campaign_url=https%3A%2F%2Fus.puma.com%2Fus%2Fen%3Fgclid%3DEAIaIQobChMIqefu28ua_QIVA7jICh2-mQoGEAAYASAAEgKZH_D_BwE; __gtm_referrer=https%3A%2F%2Fwww.google.com%2F; _gaexp=GAX1.2.xPR9TwuDQOap3w71j8N6Bw.19473.0!qUrzfIDDRHOHZlmIn2Oi_Q.19494.1; _gcl_aw=GCL.1676578142.EAIaIQobChMIqefu28ua_QIVA7jICh2-mQoGEAAYASAAEgKZH_D_BwE; _gcl_au=1.1.1621997984.1676569408; _ga_BD2CHD3FVE=GS1.1.1676577848.3.1.1676581713.60.0.0; _ga=GA1.2.783642839.1676569409; _ga_FDZWDZJ2FL=GS1.1.1676577848.3.1.1676581713.60.0.0; _imp_apg_r_=%7B%22c%22%3A%22aFlyT1JzVW1lVUNyNWkyMw%3D%3DN8WBIWHBK9CMhu4w3eQYVfFl4qWjTuUTEHGg9LpyEccBgvY7-t-2AsNyt0_Zj-3l4nj_4s5hta3H7Y89VB9Dp4qz7wj5_TjaJF2x6dYFflfwkvasSUbYNqE%3D%22%2C%22dc%22%3A%22ine%22%2C%22mf%22%3A0%7D; _br_uid_2=uid%3D3596857681154%3Av%3D12.0%3Ats%3D1676569409059%3Ahc%3D9; _scid=9977bdad-6031-4a95-9045-ac5be6459635; cjConsent=MHxOfDB8Tnww; gclidLast=EAIaIQobChMIqefu28ua_QIVA7jICh2-mQoGEAAYASAAEgKZH_D_BwE; cjUser=c036cf1f%2Daf5f%2D4212%2Db9d7%2D63efb26ff20c; _pin_unauth=dWlkPU5EazFZbU01T1RZdFlUQmlNQzAwWkdRMExXRmlObVl0TTJFMk4yVmpOekV4WXpZeA; _cs_c=0; _cs_id=d57a978c-45aa-ab7b-9c3b-738914ff2ead.1676569410.3.1676580111.1676577841.1593014206.1710733410879; _gid=GA1.2.1017246664.1676569411; _gac_UA-49440260-8=1.1676578143.EAIaIQobChMIqefu28ua_QIVA7jICh2-mQoGEAAYASAAEgKZH_D_BwE; scarab.visitor=%22FF1DCAD525ED858%22; _sctr=1|1676527200000; _gac_UA-49440260-37=1.1676578142.EAIaIQobChMIqefu28ua_QIVA7jICh2-mQoGEAAYASAAEgKZH_D_BwE; _tt_enable_cookie=1; _ttp=zcdmIF9nEEilLBc7dF8rNIrQ2EK; cto_bundle=MT00_l84OEc0NFJOYnc2enhEYTFweHlNMkxIS1hZZENlanclMkJWVko1NDE3THRXdUd4NEdjbko4Y1FJbU1nbUVSYnBmT21GRlIwNDBzSkRBQzYxRzg0U1glMkZJWUFOYzROZVB4RThNWnNHbHJ0bG5vcFc0UkZCdFZRczBEVFllYmVYd0RzdGw; _fbp=fb.1.1676569414039.1413134748; usbls=1; OptanonConsent=groups%3DC0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1; scarab.profile=%22384146_01%7C1676574255%22; BVBRANDID=492ffa20-986a-450f-a337-8d4591f1c3da; _cs_s=13.0.0.1676581911652; _uetsid=6c59a240ae2111ed8dc7375211d041ea; _uetvid=6c59b720ae2111edba71cdfa61583391",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
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
