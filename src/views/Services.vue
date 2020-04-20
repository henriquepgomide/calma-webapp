<template>
  <div class="services">
    <vue-headful
      :title="$t('services_page_title_seo')"
      :description="$t('services_page_description_seo')"
    />
      <section class="section">
	<div class="container">
	  <h1 class="title">{{ $t("services_page_header") }}</h1>
	  <p class="is-size-5">{{ $t("services_page_description") }}</p>
	</div>
      </section>
        <section class="section">
      <div class="container">
	{{services[1]}}
	<h1>Hello Component</h1>
	<b-table 
	   :data="services"
	   :columns="columns">
	</b-table>
      </div>
    </section>
  </div>
</template>
<script>
import services from "../assets/data/services_list.json";

export default {
  data() {
    return {
      services,
      columns: [
	{
	  field: "name",
	  label: "Serviço"
	},
	{
	  field: "covid_related",
	  label: "Específico COVID-19"
	},
	{
	  field: "has_urgency",
	  label: "Atende urgência?"
	},
	{
	  field: "service_url",
	  label: "Link"
	},


      ]
    }
  }
}
</script>
