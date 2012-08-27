var T_FADEOUT = 250;
var T_FADEIN = 500;


//when user clicks on one of the tabs, the so-called "tab change" is triggered. While in progress we must
//assure that no other tab change begins or else we get undesired behavior (i.e. two tab contents displayed
//at the same time). To prevent this we check the tab_changing flag upon each click and if it is set to true,
//click is ignored. If it is set to false, a lock is acquired (by setting it to true) and then released when
//tab change effect is finished.
var tab_changing = false;

var active_tab = 0;   //tab that is currently active (displayed)


 $(document).ready(function() {
   //at the beginning hide all but first tab (which should be set to "selected"
   $("#content_2").css("display", "none");
   $("#content_3").css("display", "none");
   $("#tab_1_li").addClass("tab_selected");

   //set onclick for sliding
   $("#tab_1_a").click(function(e) {
            e.preventDefault();
            if (active_tab == 1) {
                return;   //no need to change anything, this tab is already active (displayed)
            }

            if (tab_changing) {
                return;  //if a tab is currently being changed, do nothing
            }
            else {
                tab_changing = true;  //mark that a tab is being changed at the moment
            }

            //change active tab's style
            $("#tab_1_li").addClass("tab_selected");
            $("#tab_2_li").removeClass("tab_selected");
            $("#tab_3_li").removeClass("tab_selected");

            $("#content_2").fadeOut(T_FADEOUT);
            $("#content_3").fadeOut(T_FADEOUT);
            //add 10ms to T_FADEOUT to make sure that the other two tab contents have completely disappeared
            setTimeout('$("#content_1").fadeIn(T_FADEIN)', T_FADEOUT + 10);

            //after tab change is complete, tab_changing lock needs to be released
            setTimeout('tab_changing = false; active_tab = 1;', T_FADEOUT + T_FADEIN);
        });

   $("#tab_2_a").click(function(e) {
            e.preventDefault();
            if (active_tab == 2) {
                return;   //no need to change anything, this tab is already active (displayed)
            }

            if (tab_changing) {
                return;  //if a tab is currently being changed, do nothing
            }
            else {
                tab_changing = true;  //mark that a tab is being changed at the moment
            }

            //change active tab's style
            $("#tab_2_li").addClass("tab_selected");
            $("#tab_1_li").removeClass("tab_selected");
            $("#tab_3_li").removeClass("tab_selected");

            $("#content_1").fadeOut(T_FADEOUT);
            $("#content_3").fadeOut(T_FADEOUT);
            //add 10ms to T_FADEOUT to make sure that the other two tab contents have completely disappeared
            setTimeout('$("#content_2").fadeIn(T_FADEIN)', T_FADEOUT + 10);

            //after tab change is complete, tab_changing lock needs to be released
            setTimeout('tab_changing = false; active_tab = 2;', T_FADEOUT + T_FADEIN);
        });

   $("#tab_3_a").click(function(e) {
            e.preventDefault();
            if (active_tab == 3) {
                return;   //no need to change anything, this tab is already active (displayed)
            }

            if (tab_changing) {
                return;  //if a tab is currently being changed, do nothing
            }
            else {
                tab_changing = true;  //mark that a tab is being changed at the moment
            }

            //change active tab's style
            $("#tab_3_li").addClass("tab_selected");
            $("#tab_1_li").removeClass("tab_selected");
            $("#tab_2_li").removeClass("tab_selected");

            $("#content_1").fadeOut(T_FADEOUT);
            $("#content_2").fadeOut(T_FADEOUT);
            //add 10ms to T_FADEOUT to make sure that the other two tab contents have completely disappeared
            setTimeout('$("#content_3").fadeIn(T_FADEIN)', T_FADEOUT + 10);

            //after tab change is complete, tab_changing lock needs to be released
            setTimeout('tab_changing = false; active_tab = 3;', T_FADEOUT + T_FADEIN);
        });

 });    //end $(document).ready

