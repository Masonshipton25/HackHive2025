# TurtleTalk

## Introduction

Since 2008, Canada has been working toward reconciliation with Indigenous peoples, beginning with the establishment of the Truth and Reconciliation Commission (TRC). A key aspect of this effort includes the preservation of Indigenous languages and cultures (Call to Action 14) and historical records (Calls to Action 67–83). To support this, various websites have been created, including government platforms such as Indigenous Services Canada, the National Centre for Truth and Reconciliation (NCTR), and Statistics Canada, as well as Indigenous-led initiatives like the First Nations Information Governance Centre (FNIGC), FirstVoices, the Métis Nation of Canada, and Inuit Tapiriit Kanatami (ITK). While much of this data is publicly available, information is often fragmented across multiple sites, making it difficult to locate specific details on Indigenous topics. 

We are developing **TurtleTalk**, an open-source AI model, to be led by Indigenous groups, trained on Indigenous languages, cultures, and traditions. This model will serve as both a centralized repository for Indigenous knowledge—often scattered across multiple sources—and a user-friendly tool for answering questions on Indigenous topics.

With TurtleTalk, we hope to make it easier to access and retrieve information on Indigenous issues, helping to advance reconciliation through artificial intelligence. By bridging the gap between technology and tradition, TurtleTalk aims to support both Indigenous communities and non-Indigenous users in walking toward a shared future with AI hand in hand.

## Methodology

TurtleTalk is built by fine-tuning mBERT on a curated dataset of Indigenous languages, cultures, and traditions. mBERT was chosen for its multilingual capabilities and proven effectiveness in fine-tuning for low-resource languages, making it well-suited for Indigenous language processing.

The dataset is sourced from The Canadian Encyclopedia, Statistics Canada, FirstVoices, Indigenous Services Canada, and the First Nations Information Governance Centre (FNIGC), all of which provide some publicly available data. It can be further expanded with additional sources such as Native Land Digital, the National Centre for Truth and Reconciliation (NCTR), and the Assembly of First Nations (AFN), which also offer varying levels of public data. While the dataset primarily focuses on First Nations, resources from the Métis Nation of Canada and Inuit Tapiriit Kanatami (ITK) provide data on non-First Nations Indigenous communities, some of which is publicly accessible or available upon request.