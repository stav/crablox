from fasthtml.common import A, Card, Div, Li, Ul
from fasthtml.svg import Defs, ClipPath, Rect, G, Path, Text, Tspan, Svg, Desc

from blocks import block

id = "IsmSrvPmi"


def srv_pmi_block(rt):

    path = "/ism/srv"

    @rt(path)
    def get():
        return Service()

    return block(path, id, "ISM Service PMI")


def Service():

    url1 = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"
    url2 = "https://tradingeconomics.com/united-states/non-manufacturing-pmi"

    card = Card(
        cls="wlv-details",
        footer=Ul(
            Li(A(url1, href=url1, target="_blank")),
            Li(A(url2, href=url2, target="_blank")),
        )
    )
    return Div(
        card,
        svg_chart2,
        id=id,
    )

# https://h2f.answer.ai/
svg_chart2 = Svg(
    Desc('Created with Highcharts 10.1.0'),
    Defs(
        ClipPath(
            Rect(x='0', y='0', width='543', height='295', fill='none'),
            id='highcharts-3lyx6p1-109-'
        ),
        ClipPath(
            Rect(x='0', y='0', width='543', height='295', fill='none'),
            id='highcharts-3lyx6p1-126-'
        ),
        ClipPath(
            Rect(x='25', y='40', width='543', height='295', fill='none'),
            id='highcharts-3lyx6p1-127-'
        )
    ),
    Rect(fill='#ffffff', x='0', y='0', width='600', height='410', rx='0', ry='0', cls='highcharts-background'),
    Rect(fill='none', x='25', y='40', width='543', height='295', cls='highcharts-plot-background'),
    G(
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 75.5 40 L 75.5 335', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 143.5 40 L 143.5 335', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 211.5 40 L 211.5 335', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 279.5 40 L 279.5 335', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 346.5 40 L 346.5 335', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 414.5 40 L 414.5 335', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 482.5 40 L 482.5 335', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 550.5 40 L 550.5 335', opacity='1', cls='highcharts-grid-line'),
        data_z_index='1',
        cls='highcharts-grid highcharts-xaxis-grid'
    ),
    G(
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 335.5 L 568 335.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 302.5 L 568 302.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 269.5 L 568 269.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 237.5 L 568 237.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 204.5 L 568 204.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 171.5 L 568 171.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 138.5 L 568 138.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 106.5 L 568 106.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 73.5 L 568 73.5', opacity='1', cls='highcharts-grid-line'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='1', stroke_dasharray='1,1', data_z_index='1', d='M 25 39.5 L 568 39.5', opacity='1', cls='highcharts-grid-line'),
        data_z_index='1',
        cls='highcharts-grid highcharts-yaxis-grid'
    ),
    Rect(fill='none', data_z_index='1', x='25', y='40', width='543', height='295', cls='highcharts-plot-border'),
    G(data_z_index='1', cls='highcharts-grid highcharts-yaxis-grid'),
    G(
        Path(fill='none', stroke='#E6E6E6', stroke_width='1', data_z_index='7', d='M 25 335.5 L 568 335.5', cls='highcharts-axis-line'),
        data_z_index='2',
        cls='highcharts-axis highcharts-xaxis'
    ),
    G(
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 335.25 L 578 335.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 302.25 L 578 302.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 269.25 L 578 269.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 237.25 L 578 237.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 204.25 L 578 204.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 171.25 L 578 171.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 138.25 L 578 138.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 106.25 L 578 106.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 73.25 L 578 73.25', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E7E7E7', stroke_width='0.5', d='M 568 39.75 L 578 39.75', opacity='1', cls='highcharts-tick'),
        Path(fill='none', stroke='#E6E6E6', stroke_width='1', data_z_index='7', d='M 568.5 40 L 568.5 335', cls='highcharts-axis-line'),
        data_z_index='2',
        cls='highcharts-axis highcharts-yaxis'
    ),
    G(
        Path(fill='none', stroke='#E6E6E6', stroke_width='1', data_z_index='7', d='M 24.5 40 L 24.5 335', cls='highcharts-axis-line'),
        data_z_index='2',
        cls='highcharts-axis highcharts-yaxis'
    ),
    G(
        G(
            Rect(x='4', y='214', width='27', height='82', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='38', y='119', width='27', height='177', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='72', y='145', width='27', height='151', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='106', y='185', width='27', height='111', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='139', y='250', width='27', height='46', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='173', y='106', width='27', height='190', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='207', y='270', width='27', height='26', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='241', y='185', width='27', height='111', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='275', y='181', width='27', height='115', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='309', y='70', width='27', height='226', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='343', y='34', width='27', height='262', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='377', y='162', width='27', height='134', fill='#4f81bd', opacity='1', cls='highcharts-point'),
            Rect(x='411', y='99', width='27', height='197', fill='rgb(205,205,205)', fill_opacity='1', opacity='1', cls='highcharts-point'),
            Rect(x='445', y='165', width='27', height='131', fill='rgb(205,205,205)', fill_opacity='1', opacity='1', cls='highcharts-point'),
            Rect(x='479', y='230', width='27', height='66', fill='rgb(205,205,205)', fill_opacity='1', opacity='1', cls='highcharts-point'),
            Rect(x='513', y='198', width='27', height='98', fill='rgb(205,205,205)', fill_opacity='1', opacity='1', cls='highcharts-point'),
            data_z_index='4',
            opacity='1',
            transform='translate(25,40) scale(1 1)',
            clip_path='url(#highcharts-3lyx6p1-126-)',
            cls='highcharts-series highcharts-series-0 highcharts-column-series'
        ),
        G(data_z_index='4', opacity='1', transform='translate(25,40) scale(1 1)', clip_path='none', cls='highcharts-markers highcharts-series-0 highcharts-column-series'),
        data_z_index='3',
        cls='highcharts-series-group'
    ),
    Text(
        'US Non Manufacturing PMI',
        Tspan('- points', style='font-size: 10px;'),
        x='24',
        text_anchor='start',
        data_z_index='4',
        style='color: rgb(51, 51, 51); font-size: 1em; fill: rgb(51, 51, 51); font-family: Helvetica;',
        y='20',
        cls='highcharts-title'
    ),
    Text('Source: tradingeconomics.com | Institute for Supply Management', x='590', text_anchor='end', data_z_index='4', style='color: rgb(51, 51, 51); fill: rgb(51, 51, 51); font-size: 0.8em; font-family: Helvetica;', y='402', cls='highcharts-subtitle'),
    Text(x='10', text_anchor='start', data_z_index='4', style='color: rgb(102, 102, 102); fill: rgb(102, 102, 102);', y='407', cls='highcharts-caption'),
    G(
        Text('2024', x='75.90625', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        Text('Mar', x='143.78125', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        Text('May', x='211.65625', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        Text('Jul', x='279.53125', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        Text('Sep', x='347.40625', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        Text('Nov', x='415.28125', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        Text('Mar', x='483.15625', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        Text('Sep', x='551.03125', style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);', text_anchor='middle', transform='translate(0,0)', y='350', opacity='1'),
        data_z_index='7',
        cls='highcharts-axis-labels highcharts-xaxis-labels'
    ),
    G(
        Text(
            Tspan('48', cls='yLabels_'),
            x='0',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            visibility='hidden'
        ),
        Text(
            Tspan('49', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='305',
            opacity='1'
        ),
        Text(
            Tspan('50', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='272',
            opacity='1'
        ),
        Text(
            Tspan('51', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='240',
            opacity='1'
        ),
        Text(
            Tspan('52', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='207',
            opacity='1'
        ),
        Text(
            Tspan('53', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='174',
            opacity='1'
        ),
        Text(
            Tspan('54', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='141',
            opacity='1'
        ),
        Text(
            Tspan('55', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='109',
            opacity='1'
        ),
        Text(
            Tspan('56', cls='yLabels_'),
            x='573',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            y='76',
            opacity='1'
        ),
        Text(
            Tspan('57', cls='yLabels_'),
            x='0',
            style='color: rgb(51, 51, 51); cursor: default; font-size: 1em; font-family: Helvetica; fill: rgb(51, 51, 51);',
            text_anchor='start',
            transform='translate(0,0)',
            visibility='hidden'
        ),
        data_z_index='7',
        cls='highcharts-axis-labels highcharts-yaxis-labels'
    ),
    G(data_z_index='7', cls='highcharts-axis-labels highcharts-yaxis-labels'),
    G(data_z_index='99', clip_path='url(#highcharts-3lyx6p1-127-)', cls='highcharts-control-points'),
    **{'xmlns:xlink':'http://www.w3.org/1999/xlink'},
    version='1.1',
    style='font-family: "Lucida Grande", "Lucida Sans Unicode", Arial, Helvetica, sans-serif; font-size: 12px;',
    xmlns='http://www.w3.org/2000/svg',
    width='600',
    height='410',
    viewbox='0 0 600 410',
    cls='highcharts-root'
)
