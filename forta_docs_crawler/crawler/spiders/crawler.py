import scrapy


class Crawler(scrapy.Spider):
    name = "crawler"
    start_urls = ['https://docs.ethers.io/v5/api/providers/provider/#Provider--account-methods',
                  "https://docs.ethers.io/v5/api/providers/jsonrpc-provider/",
                  "https://docs.ethers.io/v5/api/providers/api-providers/",
                  "https://docs.ethers.io/v5/api/providers/other/",
                  "https://docs.ethers.io/v5/api/providers/types/",
                  "https://docs.ethers.io/v5/api/signer/",
                  "https://docs.ethers.io/v5/api/contract/contract/",
                  "https://docs.ethers.io/v5/api/contract/contract-factory/",
                  "https://docs.ethers.io/v5/api/utils/abi/coder/",
                  "https://docs.ethers.io/v5/api/utils/abi/fragments/",
                  "https://docs.ethers.io/v5/api/utils/abi/interface/",
                  "https://docs.ethers.io/v5/api/utils/address/",
                  "https://docs.ethers.io/v5/api/utils/bignumber/",
                  "https://docs.ethers.io/v5/api/utils/bytes/",
                  "https://docs.ethers.io/v5/api/utils/constants/",
                  "https://docs.ethers.io/v5/api/utils/display-logic/",
                  "https://docs.ethers.io/v5/api/utils/encoding/",
                  "https://docs.ethers.io/v5/api/utils/fixednumber/",
                  "https://docs.ethers.io/v5/api/utils/hashing/",
                  "https://docs.ethers.io/v5/api/utils/hdnode/",
                  "https://docs.ethers.io/v5/api/utils/logger/",
                  "https://docs.ethers.io/v5/api/utils/properties/",
                  "https://docs.ethers.io/v5/api/utils/signing-key/",
                  "https://docs.ethers.io/v5/api/utils/strings/",
                  "https://docs.ethers.io/v5/api/utils/transactions/",
                  "https://docs.ethers.io/v5/api/utils/web/",
                  "https://docs.ethers.io/v5/api/utils/wordlists/",
                  "https://docs.ethers.io/v5/api/other/assembly/api/",
                  "https://docs.ethers.io/v5/api/other/assembly/ast/",
                  "https://docs.ethers.io/v5/api/other/hardware/",
                  "https://docs.ethers.io/v5/api/experimental/"
                  ]

    def parse(self, response):
        for methods in response.css("div.show-anchors"):
            yield {
                'api-name': methods.css("span.path::text").get(),
                'method-name': methods.css("span.method::text").get()
            }
