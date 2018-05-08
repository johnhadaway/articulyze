<!DOCTYPE html>
<html lang="en">
<head>
    <title>Sudan</title>
    <!-- stylesheets -->
    <link rel="stylesheet" href = "../css/bootstrap.min.css">
    <link rel="stylesheet" href = "../css/bootstrap-grid.css">
    <link rel="stylesheet" href = "../css/art-style.css">
    <link rel="stylesheet" href = "../css/art-country-style.css">
    <link rel="icon" href="../img/ICONS/glass.png">
    <?php
    $db = new PDO("sqlite:current_unohca.db");
    $sql = 'SELECT DISTINCT * FROM sudan WHERE days_in_db > (SELECT MAX(days_in_db) FROM sudan) - 7 ORDER BY score DESC';
    $result = $db->query($sql);
    $rowarray = $result->fetchall(PDO::FETCH_ASSOC);
    $x = 0;

    function show($rowarray){
        global $x;
        $title = $rowarray[$x]['title'];
        echo "$title";
    };
    
    function show2($rowarray){
        global $x;
        $url = $rowarray[$x]['url'];
        echo "<a class='art-div-link' href='$url'></a>";       
        $x++;
    }
    ?>
</head>
<body>
    <nav class="navbar navbar-expand navbar-dark fixed-top art-style-back-black">
      <a href="../index.html" class="pull-left"><img src="../img/vertical/navbar.png" width="35px" height="30px"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#art-navbarCollapse" aria-controls="art-navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="art-navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="../other-pages/countries.html">Countries</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="../other-pages/about.html">About</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container-fluid sudan-div-page">
        <div class="row art-style-10-height"></div>
        <div class="row">
            <div class="col-md-3 col-1"></div>
            <div class="col-md-6 col-10 art-style-back-red art-container-country">
                <p class="country-name-text text-uppercase art-unselectable">Sudan</p>
            </div>
            <div class="col-md-3 col-1"></div>
        </div>
        <div class="row art-style-15-height"></div>
        <div class="row">
            <div class="col-md-6 col-2"></div>
            <div class="col-md-5 col-8 art-style-back-red">
                <div class="row art-container-country">
                    <div class="col-12 art-style-white-3-bborder">
                        <p class="text-uppercase art-country-title-style art-unselectable">Summary:</p>
                    </div>
                    <div class="col-12">
                        <p class="art-style-text-white sec-font art-style-margins-country art-unselectable">Widespread poverty, underdevelopment, and recurrent climactic shocks, along with instances of conflict, spur food insecurity, displacement and thus the extent of Sudan’s humanitarian situation. Eastern Sudan has a particularly high rate of malnutrition. According to Sudan’s 2018 Humanitarian Needs Overview, 5.5 million people require humanitarian assistance, of whom 3.1 million are in the Darfur region. South Sudan’s conflict has contributed to this figure: 770,000 South Sudanese refugees are displaced in Sudan. Sudan is ranked 165th in the Human Development Index (2015).</p>
                    </div>
                </div>
            </div>
            <div class="col-md-1 col-2"></div>
        </div>
        <div class="row art-style-10-height"></div>
        <div class="row">
            <div class="col-md-2 col-2"></div>
            <div class="col-md-5 col-8 art-style-back-red">
                <div class="row art-container-country">
                    <p class="text-uppercase art-country-title-style art-unselectable">Articles:</p>
                </div>
                <div class="row">
                    <div class="col-3 art-number-style art-unselectable">1.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">2.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">3.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">4.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                    <div class="col-3 art-number-style art-unselectable">5.</div>
                    <div class="col-9 art-article-title-style sec-font art-hover-effect art-unselectable">
                        <?php
                            show($rowarray);
                        ?>
                        <?php
                            show2($rowarray);
                        ?>
                    </div>
                </div>
            </div>
            <div class="col-md-5 col-2"></div>
        </div>
        <div class="row art-style-20-height"></div>
    </div>
</body>
</html>