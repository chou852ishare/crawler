function() {
  var b, c = $("#j-tag-list"),
    d = $(this),
    e = d.text(),
    f = window.template,
    g = $("body").attr("data-tag"),
    h = '<li class="card" data-pn="<%= packageName %>"><a class="corner" href="/apps/<%= packageName %>"></a><div class="icon-wrap"><a href="/apps/<%= packageName %>" rel="nofollow"><img src="<%= icons["px68"] %>" with="68" height="68" alt="<%= title %>" class="icon"/></a></div><div class="app-desc"><a href="/apps/<%= packageName %>" class="name"><%= title %></a><div class="meta"><% if(apks[0].superior && apks[0].superior == 1){ %><a class="tag gooddev" href="http://developer.wandoujia.com/apps/review-guideline/" target="_blank" title="豌豆荚认证的优质开发者"></a><% } %><% if(ad){ %> <b class="promoted-text">推广</b><% } %> <span><%= installedCountStr %>人安装</span><span class="dot">・</span><span><%= apks[0].size %>B</span></div><div class="comment"><% if(snippet){ %><%= snippet %><% } %></div></div><% if(apks){ %><% if(link_type == 0){ %><% if(sem == 1){ %><a data-sem="1" data-install="<%= installedCountStr %>" data-lisk="<%= likesCount %>" data-name="<%= title %>" data-pn="<%= packageName %>" class="install-btn" rel="nofollow" href="http://apps.wandoujia.com/redirect?url=http%3A%2F%2Fdl.wandoujia.com%2Ffiles%2Fphoenix%2Flatest%2Fwandoujia-wandoujia_binded___bind___<%= packageName %>.apk&pos=mobileweb/apps/bd_bind">下载</a><% }else{ %><a data-install="<%= installedCountStr %>" data-lisk="<%= likesCount %>" data-name="<%= title %>" data-pn="<%= packageName %>" class="install-btn" rel="nofollow" href="http://apps.wandoujia.com/apps/<%= packageName %>/download" download="<%= title %>.apk">下载</a><% } %><% }else if(link_type == 1){ %><a data-install="<%= installedCountStr %>" data-lisk="<%= likesCount %>" data-name="<%= title %>" data-pn="<%= packageName %>" class="install-btn" rel="nofollow" href="http://apps.wandoujia.com/apps/<%= packageName %>/download" style="display:none;" download="<%= title %>.apk">下载</a><a href="javascript:void(0);" data-install="<%= installedCountStr %>" data-lisk="<%= likesCount %>" data-name="<%= title %>" data-pn="<%= packageName %>" data-vc="<%= apks[0].versionCode %>" class="push-btn" rel="nofollow">推送</a><% }else if(link_type == 2){ %><a data-install="<%= installedCountStr %>" data-lisk="<%= likesCount %>" data-name="<%= title %>" data-pn="<%= packageName %>" class="install-btn" rel="nofollow" <% if(isPC){ %> <% if(pcSem == 1){ %> data-track="taginfo-wdjp-<%= pcSource %>" <% }else{ %> data-track="taginfo-wdjp-<%= packageName %>" <% } %> <% } %> href="wandoujia://type=apk&wdj=1&name=<%= title %>&url=http://apps.wandoujia.com/apps/<%= packageName %>/download?pos=www/award==">下载</a><% }else if(link_type == 3){ %><a data-install="<%= installedCountStr %>" data-lisk="<%= likesCount %>" data-name="<%= title %>" data-pn="<%= packageName %>" class="install-btn" rel="nofollow" href="http://apps.wandoujia.com/apps/<%= packageName %>/download" download="<%= title %>.apk">下载</a><% } %><% } %><% if(sem == 1){ %><div class="bubble"><span class="arrow"></span>稍后将会为您自动安装「<%= title %>」</div><% } %></li>',
    i = f(h),
    j = "apps.likesCount,apps.reason,apps.ad,apps.title,apps.packageName,apps.apks.size,apps.icons.px68,apps.apks.superior,apps.installedCountStr,apps.snippet,apps.editorComment,apps.apks.versionCode",
    k = c.find(".card").length;
  b = "http://apps.wandoujia.com/api/v1/apps?ads_count=0&tag=" + g + "&max=12&start=" + k + "&opt_fields=" + j, a || (a = 1, d.text("加载中..."), $.ajax({
    url: b,
    dataType: "jsonp",
    success: function(b) {
      if (b) {
        var f = 0,
          h = "",
          j = 0,
          k = $("body").hasClass("PC"),
          l = $("body").data("sem") || 0,
          m = b[0].apps.length;
        if (0 == m) return $("#j-refresh-btn").hide(), !1;
        for (12 > m && $("#j-refresh-btn").hide(), k && (j = $.cookie("wdj_auth") ? 1 : wdInstalled ? 2 : 3); m > f; f++) {
          var n = b[0].apps[f];
          if (n.link_type = j, n.sem = 0, k || 1 != l || (n.sem = 1), n.isPC = k, k) {
            var o = window.pcSem,
              p = window.pcSource;
            n.pcSem = o, n.pcSource = p
          }
          n.editorComment && (n.snippet = n.editorComment), h += i(n)
        }
        c.append(h), d.text(e), a = 0, ga("send", "event", g, "loadmore")
      }
    }
  }))
}
