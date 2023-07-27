import {Col, Nav, NavItem, NavLink, Row} from "react-bootstrap";

export const Footer = () => {
    return (
        <div>
            <hr className="mb-0 mt-0"/>
            <footer className="bg-light p-3">
                <Row>
                    <Col>
                        <Nav>
                            <NavItem>
                                <NavLink as="span">GITHUB : <a href="https://github.com/limaoyi1">limaoyi1</a></NavLink>
                                <Nav as="ul" className="d-flex flex-column">
                                    <NavItem as="li" className="pl-0">
                                        <NavLink as="span">商业合作 : <a href="https://img1.imgtp.com/2023/07/25/FHQCWt6H.png">微信</a></NavLink>
                                    </NavItem>
                                    <NavItem as="li" className="pl-0">
                                        <NavLink as="span">交流吹水 : <a href="https://img1.imgtp.com/2023/07/25/FHQCWt6H.png">微信群</a></NavLink>
                                    </NavItem>
                                </Nav>
                            </NavItem>
                        </Nav>
                    </Col>
                    <Col>
                        <Nav>
                            <NavItem>
                                <NavLink as="span">其他产品</NavLink>
                                <Nav as="ul" className="d-flex flex-column">
                                    <NavItem as="li" className="pl-0">
                                        <NavLink href="http://www.limaoyi.top:4399/#">自动生成PPT</NavLink>
                                    </NavItem>
                                    {/*<NavItem as="li" className="pl-0">*/}
                                    {/*    <NavLink href="https://chatscope.io/demo/chat-friends/">Chat friends</NavLink>*/}
                                    {/*</NavItem>*/}
                                    {/*<NavItem as="li" className="pl-0">*/}
                                    {/*    <NavLink href="https://mars.chatscope.io/">Mars chat</NavLink>*/}
                                    {/*</NavItem>*/}
                                </Nav>
                            </NavItem>
                        </Nav>
                    </Col>
    
                    <Col>
                        <Nav>
                            <NavItem>
                                <NavLink as="span">鸣谢</NavLink>
                                <Nav as="ul" className="d-flex flex-column">
                                    <NavItem as="li" className="pl-0">
                                        <NavLink href="https://github.com/langchain-ai/langchain">langchain</NavLink>
                                    </NavItem>
                                    <NavItem as="li" className="pl-0">
                                        <NavLink href="https://github.com/chatscope/chat-ui-kit-react">chatscope</NavLink>
                                    </NavItem>
                                    <NavItem as="li" className="pl-0">
                                        <NavLink href="https://github.com/w4123/GenshinVoice">GenshinVoice</NavLink>
                                    </NavItem>
                                    <NavItem as="li" className="text-right mt-4">
                                        <strong>异界相遇!</strong>
                                    </NavItem>
                                </Nav>
                            </NavItem>
                        </Nav>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <p className="px-3 mt-4 mb-0">Genshin-GPT 基于原神对话知识库和OPENAI API生成,仅作为学习使用,未经许可,禁止转载和搬运.推荐在PC或者平板使用.</p>
                    </Col>
                </Row>
            </footer>
        </div>
    );
};