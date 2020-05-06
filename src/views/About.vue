<template>
  <div class="About">
    <vue-headful
      :title="$t('faq_page_title_seo')"
      :description="$t('faq_page_description_seo')"
    />
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
