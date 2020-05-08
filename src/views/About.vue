<template>
  <div class="About">
    <section class="section">
      <div class="container">
        <h1 class="title is-size-1">{{ $t("faq_page_title") }}</h1>
        <p class="is-size-5">{{ $t("faq_page_p") }}</p>
        <br />
        <br />

        <h1 class="is-size-4">{{ $t("faq_page_q1_h") }}</h1>
        <p class="is-size-5">{{ $t("faq_page_q1_p") }}</p>
        <br />

        <h1 class="is-size-4">{{ $t("faq_page_q2_h") }}</h1>
        <p class="is-size-5">{{ $t("faq_page_q2_p") }}</p>
        <br />

        <h1 class="is-size-4">{{ $t("faq_page_q3_h") }}</h1>
        <p class="is-size-5">{{ $t("faq_page_q3_p") }}</p>
        <br />

        <h1 class="is-size-4">{{ $t("faq_page_q4_h") }}</h1>
        <p class="is-size-5">{{ $t("faq_page_q4_p1") }}</p>
        <p class="is-size-5">{{ $t("faq_page_q4_p2") }}</p>
        <p class="is-size-5">{{ $t("faq_page_q4_p3") }}</p>
        <br />
      </div>
    </section>
  </div>
</template>
<script>
import i18n from "@/i18n";
export default {
  metaInfo: {
    title: i18n.t("faq_page_title_seo"),
    description: i18n.t("faq_page_description_seo"),
    meta: [
      { name: "og:title", content: i18n.t("faq_page_title_seo") },
      {
        name: "og:image",
        content: "https://www.calmanessahora.com.br/calma-nessa-hora.png"
      },
      { name: "og:url", content: "https://www.calmanessahora.com.br/about" },
      { name: "description", content: i18n.t("faq_page_title_seo") },
      { name: "og:description", content: i18n.t("faq_page_description_seo") }
    ]
  }
};
</script>
